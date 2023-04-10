import open3d as o3d
import numpy as np

def ConvQuatToMat(pos, ori):
  q0 = ori[0]
  q1 = ori[1]
  q2 = ori[2]
  q3 = ori[3]

  t = np.array([[pos[0]],
                  [pos[1]],
                  [pos[2]]])

  r00 = 2 * (q0 * q0 + q1 * q1) - 1
  r01 = 2 * (q1 * q2 - q0 * q3)
  r02 = 2 * (q1 * q3 + q0 * q2)
      
  r10 = 2 * (q1 * q2 + q0 * q3)
  r11 = 2 * (q0 * q0 + q2 * q2) - 1
  r12 = 2 * (q2 * q3 - q0 * q1)
      
  r20 = 2 * (q1 * q3 - q0 * q2)
  r21 = 2 * (q2 * q3 + q0 * q1)
  r22 = 2 * (q0 * q0 + q3 * q3) - 1

  R = np.array([[r00, r01, r02],
                  [r10, r11, r12],
                  [r20, r21, r22]])

  RotationMat = np.concatenate([R, t], 1)
  a = np.array([[0,0,0,1]])
  RotationMat = np.concatenate([RotationMat, a])
  return RotationMat

def ConvMatToQuat(Mat):
  tr = Mat[0][0] + Mat[1][1] + Mat[2][2]

  if tr>0:
    S = ((tr+1)**(0.5))*2
    qw = 0.25 * S
    qx = (Mat[2][1]-Mat[1][2])/S
    qy = (Mat[0][2]-Mat[2][0])/S
    qz = (Mat[1][0]-Mat[0][1])/S
  elif Mat[0][0] > Mat[1][1] and Mat[0][0] > Mat[2][2]:
    S = ((Mat[0][0]-Mat[1][1]-Mat[2][2]+1)**(0.5))*2
    qw = (Mat[2][1]-Mat[1][2])/S
    qx = 0.25 * S
    qy = (Mat[0][1]+Mat[1][0])/S
    qz = (Mat[0][2]+Mat[2][0])/S
  elif Mat[1][1] > Mat[2][2]:
    S = ((Mat[1][1]-Mat[0][0]-Mat[2][2])**(0.5))*2
    qw = (Mat[0][2]-Mat[2][0])/S
    qx = (Mat[0][1]+Mat[1][0])/S
    qy = 0.25 * S
    qz = (Mat[1][2]+Mat[2][1])/S
  else:
    S = ((Mat[2][2]-Mat[0][0]-Mat[1][1])**(0.5))*2
    qw = (Mat[1][0]-Mat[0][1])/S
    qx = (Mat[0][2]+Mat[2][0])/S
    qy = (Mat[1][2]+Mat[2][1])/S
    qz = 0.25 * S
  quat = [qw,qx,qy,qz,Mat[0][3],Mat[1][3],Mat[2][3]]
  return quat

def make_files(path1, path2):
  i=0
  use_pose1=0
  use_cloud1=0

  pos1 = [18.1301930828, 3.89046660859e-026, -14.6287624864]
  ori1 = [0.9219677706, 0.0112649160235, -0.386607342745, -0.0195771927977]

  pos2 = [-2.08976760253, 0.655534793315, -0.336082516909]
  ori2 = [0.923614945099, -0.0114040114721, 0.375851129289, 0.0744487575521]

  R = ConvQuatToMat(pos1, ori1)
  R_f = ConvQuatToMat(pos2, ori2)
  Mat = np.dot(R_f ,np.linalg.inv(R))
  clouds_xyz = np.empty((0,3),float)
  print(Mat)
  print(R)
  print(R_f)
  print(np.dot(Mat,R))
  with open(path1+".txt", "r") as f:
    t = open(path1+"_chain.txt","w")
    e = open(path1+"_clouds.txt","w")
    e.write("NVM_V3\n")
    e.write("\n")
    lines = f.readlines()
    for line in lines:
      i = i+1
      if i == 3:
        aa = line.split()
        use_pose1 = int(aa[0])
        e.write(str(use_pose1)+"\n")
      if i >= 4 and i<use_pose1+4:
        aa = line.split()
        ori = [float(aa[2]),float(aa[3]),float(aa[4]),float(aa[5])]
        pos = [float(aa[6]),float(aa[7]),float(aa[8])]
        pose = ConvQuatToMat(pos, ori)
        pose = np.dot(Mat,pose)
        pose = ConvMatToQuat(pose)
        saveline=aa[0:2] + pose + aa[9:]
        for o in saveline:
          e.write(str(o)+" ")
        e.write("\n")
      if i == use_pose1 + 5:
        e.write("\n")
        bb = line.split()
        use_cloud1 = int(bb[0])
        e.write(str(use_cloud1)+"\n")
      if i >= use_pose1 + 6 and i <= use_cloud1 + use_pose1 + 5:
        cc = line.split()
        x = float(cc[0])
        y = float(cc[1])
        z = float(cc[2])
        r = int(cc[3])
        g = int(cc[4])
        b = int(cc[5])
        measurements_num = int(cc[6])
        a = 255

        clouds_xyz = np.array([[x, y, z, 1]])
        clouds_xyz = np.dot(np.linalg.inv(Mat), clouds_xyz.T)
        clouds_xyz = np.delete(clouds_xyz.T, 3, axis = 1)
        save_line = np.append(np.squeeze(clouds_xyz),cc[3:])
      
        for k in save_line:
          e.write(str(k)+" ")
        e.write("\n")

        chain_list = [140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159]
        index = []
        for j in range(measurements_num):
          index.append(int(cc[7+4*j]))
        if len(set(index) & set(chain_list)) >=8:
          for k in save_line[0:6]:
            t.write(str(k)+" ")
          t.write("\n")
    t.close()

  i=0
  use_pose2=0
  use_cloud2=0
  with open(path2+".txt", "r") as f:
    t = open(path2+"_chain.txt","w")
    e = open(path2+"_clouds.txt","w")
    e.write("NVM_V3\n")
    e.write("\n")
    lines = f.readlines()
    for line in lines:
      i = i+1
      if i == 3:
        aa = line.split()
        use_pose2 = int(aa[0])
        e.write(str(use_pose2)+"\n")
      if i >= 4 and i<use_pose2+5:
        e.write(line)
      if i == use_pose2 + 5:
        bb = line.split()
        use_cloud2 = int(bb[0])
        e.write(str(use_cloud2)+"\n")
      if i >= use_pose2 + 6 and i <= use_cloud2 + use_pose2 + 5:
        cc = line.split()
        measurements_num = int(cc[6])

        for k in cc:
          e.write(str(k)+" ")
        e.write("\n")

        chain_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
        index = []
        for j in range(measurements_num):
          index.append(int(cc[7+4*j]))
        if len(set(index) & set(chain_list)) >=8:
          save_line = cc[0:6]
          for k in save_line[0:6]:
            t.write(str(k)+" ")
          t.write("\n")

    t.close()
    print(use_cloud1,use_cloud2)

  pcd1 = o3d.io.read_point_cloud(path1+"_chain.txt", format="xyz")
  pcd2 = o3d.io.read_point_cloud(path2+"_chain.txt", format="xyz")
  o3d.io.write_point_cloud(path1+"_pcd.ply", pcd1)
  o3d.io.write_point_cloud(path2+"_pcd.ply", pcd2)