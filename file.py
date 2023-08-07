t = open("/home/chang/map_merge/Mapping_result/map11_building.txt", "w")

with open("/home/chang/map_merge/Mapping_result/map11_c.txt","r") as f:
  lines = f.readlines()
  for i, line in enumerate(lines):
    cc = line.split()
    x = float(cc[0])
    y = float(cc[1])
    z = float(cc[2])
    r = int(cc[3])
    g = int(cc[4])
    b = int(cc[5])
    if r == 255 and g == 255 and b == 255 :
      t.write(line)

t = open("/home/chang/map_merge/Mapping_result/merge_building.txt", "w")

with open("/home/chang/map_merge/Mapping_result/merge!.txt","r") as f:
  lines = f.readlines()
  for i, line in enumerate(lines):
    cc = line.split()
    x = float(cc[0])
    y = float(cc[1])
    z = float(cc[2])
    r = int(cc[3])
    g = int(cc[4])
    b = int(cc[5])
    if r == 255 and g == 255 and b == 255 :
      t.write(line)


t = open("/home/chang/map_merge/Mapping_result/map7_building.txt", "w")

with open("/home/chang/map_merge/Mapping_result/map7_c.txt","r") as f:
  lines = f.readlines()
  for i, line in enumerate(lines):
    cc = line.split()
    x = float(cc[0])
    y = float(cc[1])
    z = float(cc[2])
    r = int(cc[3])
    g = int(cc[4])
    b = int(cc[5])
    if r == 255 and g == 255 and b == 255 :
      t.write(line)

t = open("/home/chang/map_merge/Mapping_result/map9_building.txt", "w")

with open("/home/chang/map_merge/Mapping_result/map9_c.txt","r") as f:
  lines = f.readlines()
  for i, line in enumerate(lines):
    cc = line.split()
    x = float(cc[0])
    y = float(cc[1])
    z = float(cc[2])
    r = int(cc[3])
    g = int(cc[4])
    b = int(cc[5])
    if r == 255 and g == 255 and b == 255 :
      t.write(line)

t = open("/home/chang/map_merge/Mapping_result/map10_building.txt", "w")

with open("/home/chang/map_merge/Mapping_result/map10_c.txt","r") as f:
  lines = f.readlines()
  for i, line in enumerate(lines):
    cc = line.split()
    x = float(cc[0])
    y = float(cc[1])
    z = float(cc[2])
    r = int(cc[3])
    g = int(cc[4])
    b = int(cc[5])
    if r == 255 and g == 255 and b == 255 :
      t.write(line)

t = open("/home/chang/map_merge/Mapping_result/map12_building.txt", "w")

with open("/home/chang/map_merge/Mapping_result/map12_c.txt","r") as f:
  lines = f.readlines()
  for i, line in enumerate(lines):
    cc = line.split()
    x = float(cc[0])
    y = float(cc[1])
    z = float(cc[2])
    r = int(cc[3])
    g = int(cc[4])
    b = int(cc[5])
    if r == 255 and g == 255 and b == 255 :
      t.write(line)

t = open("/home/chang/map_merge/Mapping_result/map13_building.txt", "w")

with open("/home/chang/map_merge/Mapping_result/map13_c.txt","r") as f:
  lines = f.readlines()
  for i, line in enumerate(lines):
    cc = line.split()
    x = float(cc[0])
    y = float(cc[1])
    z = float(cc[2])
    r = int(cc[3])
    g = int(cc[4])
    b = int(cc[5])
    if r == 255 and g == 255 and b == 255 :
      t.write(line)
