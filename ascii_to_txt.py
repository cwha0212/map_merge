import numpy as np
Mat = np.array(
[[0.022234909236, -0.061623606831, -0.997851788998, 262.818847656250],
[-0.049073722214, -0.996962666512, 0.060475200415, -2.203369617462],
[-0.998547613621, 0.047623638064, -0.025191474706, -514.876708984375],
[0.000000000000, 0.000000000000, 0.000000000000, 1.000000000000]]
)
t = open("/home/chang/map_merge/hand/map5_new.txt", "w")
with open("/home/chang/map_merge/hand/map5_c.txt", "r") as f:
  lines = f.readlines()
  for line in lines:
    cc = line.split()
    x = float(cc[0])
    y = float(cc[1])
    z = float(cc[2])
    r = int(cc[3])
    g = int(cc[4])
    b = int(cc[5])
    clouds_xyz = np.array([[x, y, z, 1]])

    clouds_xyz = np.dot(Mat, clouds_xyz.T)

    # clouds_xyz = np.dot(np.linalg.inv(Mat), clouds_xyz)
    clouds_xyz = np.delete(clouds_xyz.T, 3, axis = 1)
    save_line = np.append(np.squeeze(clouds_xyz),cc[3:])
      
    for k in save_line:
      t.write(str(k)+" ")
    t.write("\n")
  t.close()
