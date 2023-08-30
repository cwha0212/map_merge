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

polygon = [[-313.088, 8.54129, -31.9888], [-248.839, 8.89882, 55.6756], [-562.705, 8.32941, 102.839], [-573.706, -17.2349, 27.1067], [-313.088, 8.54129, -31.9888]]

t = open("/home/chang/map_merge/newnew/polygon/merge_map4.txt","w")
with open("/home/chang/map_merge/newnew/t/merge.txt", "r") as f:
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

polygon = [[-20.1204, 25.795, 326.777], [-45.7607, -15.8896, -113.915], [18.9112, -8.58383, -97.6742], [113.553, 15.4375, 252.806], [-20.1204, 25.795, 326.777]]

t = open("/home/chang/map_merge/newnew/polygon/map4_merge.txt","w")
with open("/home/chang/map_merge/newnew/map4_c.txt", "r") as f:
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