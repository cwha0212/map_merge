import numpy as np
import open3d as o3d
import teaserpp_python
import numpy as np 
import copy
from helpers import *

def resizing(pcd1_path, pcd2_path):
    # 첫 번째 point cloud와 두 번째 point cloud 불러오기
    pcd1 = o3d.io.read_point_cloud(pcd1_path)
    pcd2 = o3d.io.read_point_cloud(pcd2_path)
    o3d.visualization.draw_geometries([pcd1,pcd2])
    # 첫 번째 point cloud의 중심 계산
    o3d.visualization.draw_geometries([pcd1,pcd2])
    center1 = pcd1.get_center()
    # 두 번째 point cloud의 중심 계산
    center2 = pcd2.get_center()
    # 첫 번째 point cloud에서 중심까지의 평균 거리 계산
    mean_distance1 = np.mean(np.linalg.norm(np.asarray(pcd1.points) - center1, axis=1))

    # 두 번째 point cloud에서 중심까지의 평균 거리 계산
    mean_distance2 = np.mean(np.linalg.norm(np.asarray(pcd2.points) - center2, axis=1))

    # scale factor 계산
    scale_factor = mean_distance1 / mean_distance2

    # 두 번째 point cloud를 scale 조정
    pcd2.scale(scale_factor, center2)
    o3d.visualization.draw_geometries([pcd1,pcd2])
    return center2, scale_factor, pcd1, pcd2

def teaser_ICP(pcd1, pcd2):
    VOXEL_SIZE = 0.5
    VISUALIZE = True
    pcd1.paint_uniform_color([0.0, 0.0, 1.0]) # show A_pcd in blue
    pcd2.paint_uniform_color([1.0, 0.0, 0.0]) # show B_pcd in red
    if VISUALIZE:
        o3d.visualization.draw_geometries([pcd1,pcd2]) # plot A and B 

    # voxel downsample both clouds
    A_pcd = pcd1.voxel_down_sample(voxel_size=VOXEL_SIZE)
    B_pcd = pcd2.voxel_down_sample(voxel_size=VOXEL_SIZE)
    if VISUALIZE:
        o3d.visualization.draw_geometries([A_pcd,B_pcd]) # plot downsampled A and B 

    A_xyz = pcd2xyz(A_pcd) # np array of size 3 by N
    B_xyz = pcd2xyz(B_pcd) # np array of size 3 by M

    # extract FPFH features
    A_feats = extract_fpfh(A_pcd,VOXEL_SIZE)
    B_feats = extract_fpfh(B_pcd,VOXEL_SIZE)

    # establish correspondences by nearest neighbour search in feature space
    corrs_A, corrs_B = find_correspondences(
        A_feats, B_feats, mutual_filter=True)
    A_corr = A_xyz[:,corrs_A] # np array of size 3 by num_corrs
    B_corr = B_xyz[:,corrs_B] # np array of size 3 by num_corrs

    num_corrs = A_corr.shape[1]
    print(f'FPFH generates {num_corrs} putative correspondences.')

    # visualize the point clouds together with feature correspondences
    points = np.concatenate((A_corr.T,B_corr.T),axis=0)
    lines = []
    for i in range(num_corrs):
        lines.append([i,i+num_corrs])
    colors = [[0, 1, 0] for i in range(len(lines))] # lines are shown in green
    line_set = o3d.geometry.LineSet(
        points=o3d.utility.Vector3dVector(points),
        lines=o3d.utility.Vector2iVector(lines),
    )
    line_set.colors = o3d.utility.Vector3dVector(colors)
    o3d.visualization.draw_geometries([A_pcd,B_pcd,line_set])

    # robust global registration using TEASER++
    NOISE_BOUND = VOXEL_SIZE
    teaser_solver = get_teaser_solver(NOISE_BOUND)
    teaser_solver.solve(A_corr,B_corr)
    solution = teaser_solver.getSolution()
    R_teaser = solution.rotation
    t_teaser = solution.translation
    T_teaser = Rt2T(R_teaser,t_teaser)

    # Visualize the registration results
    A_pcd_T_teaser = copy.deepcopy(A_pcd).transform(T_teaser)
    o3d.visualization.draw_geometries([A_pcd_T_teaser,B_pcd])

    # local refinement using ICP
    icp_sol = o3d.pipelines.registration.registration_icp(
        A_pcd, B_pcd, NOISE_BOUND, T_teaser,
        o3d.pipelines.registration.TransformationEstimationPointToPoint(),
        o3d.pipelines.registration.ICPConvergenceCriteria(max_iteration=100))
    T_icp = icp_sol.transformation
    print(T_icp)
    # visualize the registration after ICP refinement
    A_pcd_T_icp = copy.deepcopy(A_pcd).transform(T_icp)
    o3d.visualization.draw_geometries([A_pcd_T_icp,B_pcd])

    return T_icp
