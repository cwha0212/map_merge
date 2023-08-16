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

polygon = [[-89.63, -0.938, 16.8687], [-113.748, -17.7684, -17.3423], [-11.1496, -29.8788, -71.096], [4.15818, -10.0477, -29.4245], [-89.63, -0.938, 16.8687]]

t = open("/home/chang/map_merge/new/polygon/map8_merge.txt","w")
with open("/home/chang/map_merge/new/map8_c.txt", "r") as f:
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

polygon = [[-598.694, 101.543, 285.524], [-609.457, 107.057, 211.526], [-503.815, 88.7533, 204.155], [-503.81, 92.908, 255.193], [-598.694, 101.543, 285.524]]

t = open("/home/chang/map_merge/new/polygon/merge_map8.txt","w")
with open("/home/chang/map_merge/new/t/merge.txt", "r") as f:
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