import numpy as np

def ConvQuatToMat(pos, ori):
  qw = ori[0]
  qx = ori[1]
  qy = ori[2]
  qz = ori[3]

  t = np.array([[pos[0]],
                  [pos[1]],
                  [pos[2]]])

  r00 = 2 * (qw * qw + qx * qx) - 1
  r01 = 2 * (qx * qy - qw * qz)
  r02 = 2 * (qx * qz + qw * qy)
      
  r10 = 2 * (qx * qy + qw * qz)
  r11 = 2 * (qw * qw + qy * qy) - 1
  r12 = 2 * (qy * qz - qw * qx)
      
  r20 = 2 * (qx * qz - qw * qy)
  r21 = 2 * (qy * qz + qw * qx)
  r22 = 2 * (qw * qw + qz * qz) - 1

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

pos1 = [-598.2917309779228, 5.104144325459525, 186.8865009631444]
ori1 = [-0.023987963855463017, 0.014702837405846325, 0.7830422800927407, -0.09663709210715635]

pos2 = [-57.652271271, 5.435368538, 30.227705002]
ori2 = [0.370194495, -0.001984978, -0.9152807, 0.158787265]

R_f = ConvQuatToMat(pos1, ori1)
R = ConvQuatToMat(pos2, ori2)
Mat = np.dot(R_f ,np.linalg.inv(R))
clouds_xyz = np.empty((0,3),float)
e = open("/home/chang/map_merge/orig/map8_t.txt","w")

with open("/home/chang/map_merge/new/map8_c.txt", "r") as f:
  lines = f.readlines()
  for line in lines:
    aa = line.split()
    x = float(aa[0])
    y = float(aa[1])
    z = float(aa[2])
    clouds_xyz = np.array([[x, y, z, 1]])

    clouds_xyz = np.dot(Mat, clouds_xyz.T)
    clouds_xyz = np.delete(clouds_xyz.T, 3, axis = 1)
    save_line = np.append(np.squeeze(clouds_xyz),aa[3:])
    for i in save_line:
      e.write(str(i)+ " ")
    e.write("\n")

t = open("/home/chang/map_merge/orig/map8_cam_t.txt","w")

with open("/home/chang/map_merge/orig/map8_cam.txt", "r") as f:
  lines = f.readlines()
  i = 0
  for line in lines:
    print(i)
    if i == 0:
      t.write("#timestamp x y z q_x q_y q_z q_w\n")
      i+=1
      print(i)
    else :
      aa = line.split()
      x = float(aa[1])
      y = float(aa[2])
      z = float(aa[3])
      qw = float(aa[7])
      qx = float(aa[4])
      qy = float(aa[5])
      qz = float(aa[6])
      pos = [x, y, z]
      ori = [qw, qx, qy, qz]
      R = ConvQuatToMat(pos,ori)
      R_f = np.dot(Mat, R)
      Q = ConvMatToQuat(R_f)
      save_line = [0.000000, " ", Q[4], " ",Q[5], " ",Q[6], " ",Q[1], " ",Q[2], " ",Q[3], " ",Q[0]]
      for i in save_line:
        t.write(str(i))
      t.write("\n")