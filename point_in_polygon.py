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

polygon = [[-232.543, 35.3875, 282.981], [-245.99, 24.594, 212.14], [-389.523, 17.8512, 223.404], [-387.559, -91.9851, 410.015], [-232.543, 35.3875, 282.981]]

t = open("/home/chang/map_merge/Mapping_result/polygon/merge_map11.txt","w")
with open("/home/chang/map_merge/Mapping_result/merge!.txt", "r") as f:
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

polygon = [[7.0339, -37.4379, -158.755], [-81.0832, -20.0473, -179.583], [-74.9699, -13.4941, -18.3176], [-33.1969, -7.91998, -31.6088], [7.0339, -37.4379, -158.755]]

t = open("/home/chang/map_merge/Mapping_result/polygon/map11_merge.txt","w")
with open("/home/chang/map_merge/Mapping_result/map11_building.txt", "r") as f:
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