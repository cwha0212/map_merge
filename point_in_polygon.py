def inside_or_outside(polygon, point):
    N = len(polygon)-1
    counter = 0
    p1 = polygon[0]
    for i in range(1, N+1):
        p2 = polygon[i%N]
        if point[2] > min(p1[2], p2[2]) and point[2] <= max(p1[2], p2[2]) and point[0] <= max(p1[0], p2[0]) and p1[2] != p2[2]:
            xinters = (point[2]-p1[2])*(p2[0]-p1[0])/(p2[2]-p1[2]) + p1[0]
            if(p1[0]==p2[0] or point[0]<=xinters):
                counter += 1
        p1 = p2 
    if counter % 2 == 0:
        res = False
    else:
        res = True
    return res

# polygon = [[-597.533, 16.3733, 241.288], [-625.792, 0.364876, 182.195], [-546.019, 10.638, 170.088], [-534.834, 12.8391, 201.467], [-597.533, 16.3733, 241.288]]

# t = open("/home/chang/map_merge/newnew/polygon/merge_map8.txt","w")
# with open("/home/chang/map_merge/newnew/t/merge.txt", "r") as f:
#     lines = f.readlines()
#     for i, line in enumerate(lines):
#         cc = line.split()
#         x = float(cc[0])
#         y = float(cc[1])
#         z = float(cc[2])
#         r = int(cc[3])
#         g = int(cc[4])
#         b = int(cc[5])
#         if inside_or_outside(polygon, [x,y,z]) :
#             t.write(str(x) + " " + str(y) + " " + str(z) + " " + str(r) + " " + str(g) + " " + str(b) + "\n")

# polygon = [[-89.63, -0.938, 16.8687], [-113.748, -17.7684, -17.3423], [-11.1496, -29.8788, -71.096], [4.15818, -10.0477, -29.4245], [-89.63, -0.938, 16.8687]]

# t = open("/home/chang/map_merge/newnew/polygon/map8_merge.txt","w")
# with open("/home/chang/map_merge/newnew/map8_c.txt", "r") as f:
#     lines = f.readlines()
#     for i, line in enumerate(lines):
#         cc = line.split()
#         x = float(cc[0])
#         y = float(cc[1])
#         z = float(cc[2])
#         r = int(cc[3])
#         g = int(cc[4])
#         b = int(cc[5])
#         if inside_or_outside(polygon, [x,y,z]) :
#             t.write(str(x) + " " + str(y) + " " + str(z) + " " + str(r) + " " + str(g) + " " + str(b) + "\n")

polygon = [[-23.1133, 6.3197, 133.8827], [105.8279, -5.0491, 134.2709], [119.9074, -21.0354, 55.2433], [113.2283, -28.8703, -14.9833], [-25.3249, -15.9216, -25.2696], [-71.445, 0.9623, 62.2675], [-23.1133, 6.3197, 133.8827]]
t = open("/home/chang/map_merge/hand/map1_new.txt","w")
with open("/home/chang/map_merge/hand/map1_c.txt", "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        cc = line.split()
        x = float(cc[0])
        y = float(cc[1])
        z = float(cc[2])
        r = int(cc[3])
        g = int(cc[4])
        b = int(cc[5])
        if inside_or_outside(polygon, [x,y,z]) :
            t.write(str(x) + " " + str(y) + " " + str(z) + " " + str(r) + " " + str(g) + " " + str(b) + "\n")
# polygon = [[1.81095, 3.65013, 25.2838], [8.34441, 4.54556, 71.7979], [-83.3487, 5.42319, 65.5876], [-79.9018, -0.309265, 21.4677], [1.81095, 3.65013, 25.2838]]

# t = open("/home/chang/map_merge/Mapping_result/new_polygon/map8_map6.txt","w")
# with open("/home/chang/map_merge/Mapping_result/new_transformed/map8_transformed.txt", "r") as f:
#     lines = f.readlines()
#     for i, line in enumerate(lines):
#         cc = line.split()
#         x = float(cc[0])
#         y = float(cc[1])
#         z = float(cc[2])
#         r = int(cc[3])
#         g = int(cc[4])
#         b = int(cc[5])
#         if inside_or_outside(polygon, [x,y,z]) :
#             t.write(str(x) + " " + str(y) + " " + str(z) + " " + str(r) + " " + str(g) + " " + str(b) + "\n")

# polygon = [[-59.1637, 1.78993, 63.3466], [5.31772, 17.793, 70.7281], [6.25929, -20.5368, -17.9732], [-19.9337, -17.0671, -21.3606], [-59.1637, 1.78993, 63.3466]]
# t = open("/home/chang/map_merge/Mapping_result/polygon/map3_map7.txt","w")
# with open("/home/chang/map_merge/Mapping_result/map6_c.txt", "r") as f:
#     lines = f.readlines()
#     for i, line in enumerate(lines):
#         cc = line.split()
#         x = float(cc[0])
#         y = float(cc[1])
#         z = float(cc[2])
#         r = int(cc[3])
#         g = int(cc[4])
#         b = int(cc[5])
#         if inside_or_outside(polygon, [x,y,z]) :
#             t.write(str(x) + " " + str(y) + " " + str(z) + " " + str(r) + " " + str(g) + " " + str(b) + "\n")