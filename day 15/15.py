import os
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_path, "input.txt"), "r") as f:
    _input = f.read()

lines = _input.split("\n")

y_index = 2000000

split = [i.split(":") for i in lines]

split = [[i.replace("Sensor at x=", ""), j.replace(" closest beacon is at x=", "")] for i, j in split]
split = [[[int(k) for k in i.split(", y=")], [int(l) for l in j.split(", y=")]] for i, j in split]

print(split)

Set = set()

for pair in split:
    sensor, beacon = pair
    xdiff = abs(sensor[0]-beacon[0])
    ydiff = abs(sensor[1]-beacon[1])
    manhattan = xdiff + ydiff
    vert = abs(sensor[1] - y_index)
    horiz = manhattan - vert
    if horiz < 0:
        continue
    left_edge = sensor[0] - horiz
    right_edge = sensor[0] + horiz
    print("")
    print(left_edge)
    print(right_edge)
    Set.update(range(left_edge, right_edge))

print(len(Set))

