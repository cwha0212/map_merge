from make_files import *
from teaserpp import *
import numpy as np

path1 = "/home/chang/map_merge/7eng"
path2 = "/home/chang/map_merge/engfactory"

pos1 = [-23.0780832778,-0.0202448357426,10.1999821029]
ori1 = [0.826162059389,-0.0211078304103,0.562866538945,-0.0138420562075]

pos2 = [54.4009407779,0.102018600218,-31.8319075869]
ori2 = [0.994243274731,-0.0534384469865,-0.0922518295111,0.0106869106612]

make_files(path1,path2)
center, scale, pcd1, pcd2 = resizing(path1+"_pcd.ply",path2+"_pcd.ply")

matrix = teaser_ICP(pcd1,pcd2)

i = 0
use_pose = 0
use_cloud = 0
clouds_xyz = np.empty((0,3),float)
clouds_rgb = np.empty((0,4),int)

with open(path1+"_clouds.txt", "r") as f:
  lines = f.readlines()
  for line in lines:
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
      use_cloud +=1
one = np.ones((use_cloud, 1))
clouds_xyz = np.concatenate([clouds_xyz, one], 1)
clouds_xyz = np.dot(matrix, clouds_xyz.T)
clouds_xyz = np.delete(clouds_xyz.T, 3, axis = 1)
clouds = np.concatenate([clouds_xyz, clouds_rgb], 1)

i = 0
use_pose = 0
use_cloud = 0
clouds_xyz = np.empty((0,3),float)
clouds_rgb = np.empty((0,4),int)

with open(path2+"_clouds.txt", "r") as f:
  lines = f.readlines()
  for line in lines:
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
      use_cloud +=1

clouds_xyz = clouds_xyz - center
clouds_xyz = clouds_xyz*scale
clouds_xyz = clouds_xyz + center
clouds_f = np.concatenate([clouds_xyz, clouds_rgb], 1)
clouds = np.concatenate([clouds, clouds_f], 0)

np.savetxt("clouds.txt", clouds, fmt='%f', delimiter=' ')