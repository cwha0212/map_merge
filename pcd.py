import open3d as o3d



t = open("/home/chang/map_merge/map1.txt", "w")
with open("/home/chang/map_merge/map1_c.txt", "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        cc = line.split()
        x = float(cc[0])
        y = float(cc[1])
        z = float(cc[2])
        r = int(cc[3])
        g = int(cc[4])
        b = int(cc[5])
        r = r/255
        g = g/255
        b = b/255
        t.write(str(x)+ " "+str(y) + " "+str(z) + " "+str(r) + " "+str(g) + " "+str(b) + "\n")


pcd1 = o3d.io.read_point_cloud("/home/chang/map_merge/map1.txt", format="xyzrgb")
o3d.visualization.draw_geometries([pcd1])
o3d.io.write_point_cloud("/home/chang/map_merge/map1_pcd.pcd", pcd1)

o3d.io.write_point_cloud("/home/chang/map_merge/map1_pcd.ply", pcd1)

