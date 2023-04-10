from make_files import *
from teaserpp import *
import numpy as np

path1 = "/home/chang/map_merge/fact_6/6eng"
path2 = "/home/chang/map_merge/fact_6/engfactory"

make_files(path1,path2)
center, scale, pcd1, pcd2 = resizing(path1+"_pcd.ply",path2+"_pcd.ply")

matrix = teaser_ICP(pcd1,pcd2)

i = 0
use_pose1 = 0
use_cloud1 = 0
clouds_xyz = np.empty((0,3),float)
clouds_rgb = np.empty((0,4),int)
save_lines = np.empty((0,11))

e = open(path1+"_result.txt","w")
e.write("NVM_V3"+"\n"+"\n")
with open(path1+"_clouds.txt", "r") as f:
  lines = f.readlines()
  for line in lines:
    i = i+1
    if i == 3:
      aa = line.split()
      use_pose1 = int(aa[0])
      e.write(str(use_pose1))
      e.write("\n")
    if i >= 4 and i<use_pose1+4:
      aa = line.split()
      aa[6] = (float(aa[6])-center[0])*scale+center[0]
      aa[7] = (float(aa[7])-center[1])*scale+center[1]
      aa[8] = (float(aa[8])-center[2])*scale+center[2]
      ori = [float(aa[2]),float(aa[3]),float(aa[4]),float(aa[5])]
      pos = [float(aa[6]),float(aa[7]),float(aa[8])]
      pose = ConvQuatToMat(pos, ori)
      pose = np.dot(np.linalg.inv(matrix),pose)
      pose = ConvMatToQuat(pose)
      save_line=aa[0:2] + pose + aa[9:]
      for p in save_line:
      # for p in aa:
        e.write(str(p) + " ")
      e.write("\n")
    if i == use_pose1 + 5:
      bb = line.split()
      use_cloud1 = int(bb[0])
      e.write("\n")
      e.write(str(use_cloud1))
      e.write("\n")
    if i >= use_pose1 + 6 and i <= use_cloud1 + use_pose1 + 5:
      cc = line.split()
      cc[0] = (float(cc[0])-center[0])*scale+center[0]
      cc[1] = (float(cc[1])-center[1])*scale+center[1]
      cc[2] = (float(cc[2])-center[2])*scale+center[2]
      x = float(cc[0])
      y = float(cc[1])
      z = float(cc[2])
      r = int(cc[3])
      g = int(cc[4])
      b = int(cc[5])
      a = 255
      xyz = np.array([[x],[y],[z],[1]])
      xyz = np.dot(matrix,xyz)
      xyz = np.delete(xyz.T,3,axis=1)
      xyz = xyz.tolist()
      for p in xyz[0]:
        e.write(str(p) + " ")
      for p in cc[3:]:
        e.write(str(p) + " ")
      e.write("\n")

i = 0
use_pose2 = 0
use_cloud2 = 0
clouds_xyz = np.empty((0,3),float)
clouds_rgb = np.empty((0,4),int)

# e = open(path2+"_result.txt","w")
# e.write("NVM_V3"+"\n"+"\n")
# with open(path2+"_clouds.txt", "r") as f:
#   lines = f.readlines()
#   for line in lines:
#     i = i+1
#     if i == 3:
#       aa = line.split()
#       use_pose2 = int(aa[0])
#       e.write(str(use_pose2))
#       e.write("\n")
#     if i >= 4 and i<use_pose2+4:
#       aa = line.split()
#       for p in aa:
#         e.write(str(p) + " ")
#       e.write("\n")
#     if i == use_pose2 + 5:
#       bb = line.split()
#       use_cloud2 = int(bb[0])
#       e.write("\n")
#       e.write(str(use_cloud2))
#       e.write("\n")
#     if i >= use_pose2 + 6 and i <= use_cloud2 + use_pose2 + 5:
#       cc = line.split()
#       save_line = cc
#       for p in save_line:
#         e.write(str(p) + " ")
#       e.write("\n")