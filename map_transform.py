import numpy as np

mat = np.array([[-8.33603841e-01,  7.21385620e-03,  5.52315668e-01, -6.58657398e+01],
 [-1.15083505e-01,  9.75703159e-01, -1.86438011e-01, -3.65076764e+00],
 [-5.40241079e-01, -2.18977865e-01, -8.12519705e-01, -2.01915216e+01],
 [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  1.00000000e+00]]
)
t = open("/home/chang/map_merge/orb/map_transformed.txt", "w")

with open("/home/chang/Downloads/Map_rgb/map_orb_c.txt", "r") as f:
  lines = f.readlines()
  for line in lines:
    word = line.split()
    x = float(word[0])
    y = float(word[1])
    z = float(word[2])
    clouds_xyz = np.array([[x,y,z,1]])

    clouds_xyz = np.dot(mat, clouds_xyz.T)
    clouds_xyz = np.delete(clouds_xyz.T, 3, axis = 1)
    save_line = np.append(np.squeeze(clouds_xyz),word[3:])

    for i in save_line:
      t.write(str(i)+" ")
    t.write("\n")