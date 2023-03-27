from make_files import *
from teaserpp import *
import numpy as np

path1 = "/home/chang/map_merge/7eng"
path2 = "/home/chang/map_merge/engfactory"

make_files(path1,path2)
center, scale, pcd1, pcd2 = resizing(path1+"_pcd.ply",path2+"_pcd.ply")

matrix = teaser_ICP(pcd1,pcd2)

i = 0
use_pose1 = 0
use_cloud1 = 0
clouds_xyz = np.empty((0,3),float)
clouds_rgb = np.empty((0,4),int)
save_lines = np.empty((0,11))

with open(path1+"_clouds.txt", "r") as f:
  lines = f.readlines()
  for line in lines:
    i = i+1
    if i == 3:
      aa = line.split()
      use_pose1 = int(aa[0])
    if i >= 4 and i<use_pose1+4:
      aa = line.split()
      ori = [float(aa[2]),float(aa[3]),float(aa[4]),float(aa[5])]
      pos = [float(aa[6]),float(aa[7]),float(aa[8])]
      pose = ConvQuatToMat(pos, ori)
      pose = np.dot(np.linalg.inv(matrix),pose)
      pose = ConvMatToQuat(pose)
      save_line=aa[0:2] + pose + aa[9:]
      save_line = np.array(save_line)
      save_line = np.expand_dims(save_line,axis=0)
      save_lines = np.append(save_lines, save_line, axis=0)
    if i == use_pose1 + 5:
      bb = line.split()
      use_cloud1 = int(bb[0])
    if i >= use_pose1 + 6 and i <= use_cloud1 + use_pose1 + 5:
      cc = line.split()
      x = float(cc[0])
      y = float(cc[1])
      z = float(cc[2])
      r = int(cc[3])
      g = int(cc[4])
      b = int(cc[5])
      a = 255
      clouds_xyz = np.append(clouds_xyz, np.array([[x, y, z]]), axis = 0)
      clouds_rgb = np.append(clouds_rgb, np.array([[r, g, b, a]]), axis = 0)

one = np.ones((use_cloud1, 1))
clouds_xyz = np.concatenate([clouds_xyz, one], 1)
clouds_xyz = np.dot(matrix, clouds_xyz.T)
clouds_xyz = np.delete(clouds_xyz.T, 3, axis = 1)
clouds = np.concatenate([clouds_xyz, clouds_rgb], 1)

i = 0
use_pose2 = 0
use_cloud2 = 0
clouds_xyz = np.empty((0,3),float)
clouds_rgb = np.empty((0,4),int)

with open(path2+"_clouds.txt", "r") as f:
  lines = f.readlines()
  for line in lines:
    i = i+1
    if i == 3:
      aa = line.split()
      use_pose2 = int(aa[0])
    if i >= 4 and i<use_pose2+4:
      aa = line.split()
      save_line = aa
      save_line = np.array(save_line)
      save_line = np.expand_dims(save_line,axis=0)
      save_lines = np.append(save_lines, save_line, axis=0)
    if i == use_pose2 + 5:
      bb = line.split()
      use_cloud2 = int(bb[0])
    if i >= use_pose2 + 6 and i <= use_cloud2 + use_pose2 + 5:
      cc = line.split()
      x = float(cc[0])
      y = float(cc[1])
      z = float(cc[2])
      r = int(cc[3])
      g = int(cc[4])
      b = int(cc[5])
      a = 255
      clouds_xyz = np.append(clouds_xyz, np.array([[x, y, z]]), axis = 0)
      clouds_rgb = np.append(clouds_rgb, np.array([[r, g, b, a]]), axis = 0)

clouds_xyz = clouds_xyz - center
clouds_xyz = clouds_xyz*scale
clouds_xyz = clouds_xyz + center
clouds_f = np.concatenate([clouds_xyz, clouds_rgb], 1)
clouds = np.concatenate([clouds, clouds_f], 0)

total_pose = use_pose1 + use_pose2
total_cloud = use_cloud1 + use_cloud2

e = open(path1+"_result.txt","w")
e.write("NVM_V3"+"\n"+"\n")
e.write(str(total_pose)+"\n")
for i in save_lines:
  for j in i:
    e.write(str(j) + " ")
  e.write("\n")
e.write("\n"+str(total_cloud)+"\n")
for i in clouds:
  for j in i:
    e.write(str(j) + " ")
  e.write("\n")

np.savetxt("merge.txt", clouds, fmt='%f', delimiter=' ')