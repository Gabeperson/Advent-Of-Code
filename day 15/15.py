import os
dir_path = os.path.dirname(os.path.realpath(__file__))
# NOTE: THIS IS A HIGHLY MEMORY INEFFICIENT WAY OF DOING THIS.
# THIS CAN USE ALMOST A FULL GIGABYTE IN MEMORY
# THIS IS BECAUSE IT WILL CREATE A SET WITH ALL THE IMPOSSIBLE SPOTS
# WHICH IS A VERY LARGE NUMBER
# BEWARE

with open(os.path.join(dir_path, "input.txt"), "r") as f:
    _input = f.read()

lines = _input.split("\n")

y_index = 2000000

split = [i.split(":") for i in lines]

split = [[i.replace("Sensor at x=", ""), j.replace(" closest beacon is at x=", "")] for i, j in split]
split = [[[int(k) for k in i.split(", y=")], [int(l) for l in j.split(", y=")]] for i, j in split]


Set = set()

# spaghetti code starts here
for pair in split:
    sensor, beacon = pair
    xdiff = abs(sensor[0]-beacon[0])  # get x dist between sensor and beacon
    ydiff = abs(sensor[1]-beacon[1])  # get y dist between sensor and beacon
    manhattan = xdiff + ydiff  # get manhattan dist between sensor and beacon
    vert = abs(sensor[1] - y_index)  # how much is the actual y strip from the sensor?
    horiz = manhattan - vert  # how much horiz do we have left?
    if horiz < 0:  # if sensor does not reach y strip, ignore this input
        continue
    left_edge = sensor[0] - horiz  # what is the very left edge of sensor edge in y strip
    right_edge = sensor[0] + horiz  # what is the very right edge of sensor edge in y strip
    #print("")
    #print(left_edge)
    #print(right_edge)
    Set.update(range(left_edge, right_edge))  # add range to set, allow set non-duplication to remove non-duplicate
                                                # values cause i'm lazy to make an algorithm to do this

print(len(Set))

