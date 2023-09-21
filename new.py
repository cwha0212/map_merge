import open3d as o3d
from helpers import *
import copy

path1 = "/home/chang/map_merge/newnew/polygon/map8_merge.txt"
path2 = "/home/chang/map_merge/newnew/polygon/merge_map8.txt"

# path1 = "/home/chang/map_merge/Mapping_result/map3_c.txt"
# path2 = "/home/chang/map_merge/Mapping_result/transformed/map2_transformed.txt"

a = open(path1,"r")
b = open(path2,"r")

pcd1 = o3d.io.read_point_cloud(path1, format="xyzrgb")
pcd2 = o3d.io.read_point_cloud(path2, format="xyzrgb")
VOXEL_SIZE = 1.8
VISUALIZE = True

# Load and visualize two point clouds from 3DMatch dataset
A_pcd_raw = pcd1
B_pcd_raw = pcd2
A_pcd_raw.paint_uniform_color([0.0, 0.0, 1.0]) # show A_pcd in blue
B_pcd_raw.paint_uniform_color([1.0, 0.0, 0.0]) # show B_pcd in red
o3d.visualization.draw_geometries([A_pcd_raw,B_pcd_raw])
A_pcd_raw.estimate_normals()
B_pcd_raw.estimate_normals()
if VISUALIZE:
    o3d.visualization.draw_geometries([A_pcd_raw,B_pcd_raw])
    o3d.visualization.draw_geometries([A_pcd_raw]) # plot A and B 
    o3d.visualization.draw_geometries([B_pcd_raw])

# voxel downsample both clouds
A_pcd = A_pcd_raw.voxel_down_sample(voxel_size=VOXEL_SIZE)
B_pcd = B_pcd_raw.voxel_down_sample(voxel_size=VOXEL_SIZE)
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
icp_sol = o3d.registration.registration_icp(
    A_pcd, B_pcd, NOISE_BOUND, T_teaser,
    o3d.registration.TransformationEstimationPointToPoint(),
    o3d.registration.ICPConvergenceCriteria(max_iteration=100))
T_icp = icp_sol.transformation
print(T_icp)
# visualize the registration after ICP refinement
A_pcd_T_icp = copy.deepcopy(A_pcd).transform(T_icp)
o3d.visualization.draw_geometries([A_pcd_T_icp,B_pcd])

Mat = T_icp

# t = open("/home/chang/map_merge/Mapping_result/new_transformed/map8_transformed.txt", "w")

# with open("/home/chang/map_merge/Mapping_result/map8_c.txt", "r") as f:
#   lines = f.readlines()
#   for line in lines:
#     word = line.split()
#     x = float(word[0])
#     y = float(word[1])
#     z = float(word[2])
#     clouds_xyz = np.array([[x,y,z,1]])

#     clouds_xyz = np.dot(mat, clouds_xyz.T)
#     clouds_xyz = np.delete(clouds_xyz.T, 3, axis = 1)
#     save_line = np.append(np.squeeze(clouds_xyz),word[3:])

#     for i in save_line:
#       t.write(str(i)+" ")
#     t.write("\n")

# t = open("/home/chang/map_merge/newnew/t/map8_t.txt", "w")

# with open("/home/chang/map_merge/newnew/map8_c.txt", "r") as f:
#   lines = f.readlines()
#   for line in lines:
#     word = line.split()
#     x = float(word[0])
#     y = float(word[1])
#     z = float(word[2])
#     clouds_xyz = np.array([[x,y,z,1]])

#     clouds_xyz = np.dot(Mat, clouds_xyz.T)
#     clouds_xyz = np.delete(clouds_xyz.T, 3, axis = 1)
#     save_line = np.append(np.squeeze(clouds_xyz),word[3:])

#     for i in save_line:
#       t.write(str(i)+" ")
#     t.write("\n")