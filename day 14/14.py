import os
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_path, "input.txt"), "r") as f:
    _input = f.read()

_input = _input.split("\n")

_input = [i.split(" -> ") for i in _input]


class BreakLoopException(Exception):
    pass


sand_start = [500, 0]

# pprint.pprint(_input)

paths_array = []
for arr in _input:
    for count, num in enumerate(arr):
        if num == arr[-1]:
            continue
        paths_array.append([[int(i) for i in num.split(",")], [int(i) for i in arr[count+1].split(",")]])
# pprint.pprint(paths_array)

xmin = 10000
xmax = 0
ymin = 10000
ymax = 0

for path in paths_array:
    for x, y in path:
        if x > xmax:
            xmax = x
        elif x < xmin:
            xmin = x
        if y > ymax:
            ymax = y
        elif y < ymin:
            ymin = y

# print(f"{xmin} {xmax} {ymin} {ymax}")

arr_x_size = xmax - xmin + 1 + 2 + 10
arr_y_size = ymax - ymin + 1 + 2 + 10

x_offset = xmin - 1 - 10
y_offset = ymin - 1 - 10

main_arr = [["."] * arr_x_size for _ in range(arr_y_size)]

added_paths_array = [[[x-x_offset, y-y_offset] for x, y in path] for path in paths_array]

#pprint.pprint(added_paths_array)

#pprint.pprint(main_arr)

for line in added_paths_array:
    x1, y1, x2, y2 = line[0][0], line[0][1], line[1][0], line[1][1]
    if x1 == x2:
        if y1 == y2:
            print("Something has gone wrong...")
            exit(-1)
        if y1 < y2:
            counter = y1
            while counter <= y2:
                main_arr[counter][x1] = "#"
                counter += 1
        else:
            counter = y2
            while counter <= y1:
                main_arr[counter][x1] = "#"
                counter += 1
    elif y1 == y2:
        if x1 < x2:
            counter = x1
            while counter <= x2:
                main_arr[y1][counter] = "#"
                counter += 1
        else:
            counter = x2
            while counter <= x1:
                main_arr[y1][counter] = "#"
                counter += 1
    else:
        print("Something has gone terribly, terribly wrong...")
        exit(-1)

for i in main_arr:
    print(i)

print(["@"] * len(main_arr[1]))

sand_start = [sand_start[0]-x_offset, sand_start[1]-y_offset]

bottom = len(main_arr)-1

counter = 0
try:
    while True:
        sand_x, sand_y = sand_start
        while True:
            if sand_y == bottom:
                raise BreakLoopException
            # check if possible to go to a location
            if main_arr[sand_y+1][sand_x] == ".":
                sand_y += 1
            elif main_arr[sand_y+1][sand_x-1] == ".":
                sand_y += 1
                sand_x -= 1
            elif main_arr[sand_y+1][sand_x+1] == ".":
                sand_y += 1
                sand_x += 1
            else:
                break
        main_arr[sand_y][sand_x] = "O"
        counter += 1
except (BreakLoopException, KeyboardInterrupt):
    pass


for i in main_arr:
    print(i)

print(counter)