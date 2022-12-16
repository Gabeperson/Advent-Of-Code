import os
import json
from functools import reduce
dir_path = os.path.dirname(os.path.realpath(__file__))

# use recursion-ish thing with three functions interlocking :)
#TODO if i have time change string comparison to enums

with open(os.path.join(dir_path, "input.txt"), "r") as f:
    _input = f.read()

packets_list = _input.split("\n\n")

print(len(packets_list))

packets_list = [i.split("\n") for i in packets_list]

packets_list = [[json.loads(i), json.loads(j)] for i, j in packets_list]
# print(packets_list)

def array(first, second):
    counter = 0
    while True:
        if len(first) <= counter and not len(second) <= counter:
            return "true"
        elif not len(first) <= counter and len(second) <= counter:
            return "false"
        elif len(first) <= counter and len(second) <= counter:
            return None
        if isinstance(first[counter], int):
            if isinstance(second[counter], int):
                resp = integer(first[counter], second[counter])
            else:
                resp = both(first[counter], second[counter])
        else:
            if isinstance(second[counter], list):
                resp = array(first[counter], second[counter])
            else:
                resp = both(first[counter], second[counter])
        if resp:
            return resp
        counter += 1

def integer(first, second):
    if first == second:
        return None
    elif first < second:
        return "true"
    else:
        return "false"

def both(first, second):
    if isinstance(first, int):
        length = len(second)
        if length == 0:
            length = 1
        first = [first] * length
    else:
        length = len(first)
        if length == 0:
            length = 1
        second = [second] * length
    resp = array(first, second)
    return resp

bool_list = []
for packet1, packet2 in packets_list:
    match array(packet1, packet2):
        case "true":
            bool_list.append(True)
        case "false":
            bool_list.append(False)
        case _:
            print("Something has gone wrong")

print(bool_list)
# total + enum_bool[0] if enum_bool[1] else total
final = 0
for count, boolean in enumerate(bool_list):
    if boolean:
        final += count+1

print(final)