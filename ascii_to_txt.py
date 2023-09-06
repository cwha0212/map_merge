import numpy as np
Mat = np.array(
[[0.558788836002, 0.178753629327, 0.809816181660, 291.747222900391],
[-0.005799327511, -0.975627779961, 0.219355463982, 0.343154907227],
[0.829289734364, -0.127269774675, -0.544133245945, -522.192260742188],
[0.000000000000, 0.000000000000, 0.000000000000, 1.000000000000]]
)
t = open("/home/chang/map_merge/hand/map8_new.txt", "w")
with open("/home/chang/map_merge/hand/map8_c.txt", "r") as f:
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
