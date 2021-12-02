from collections import namedtuple


Move = namedtuple('Move', 'dir val')


with open('input.txt', 'r') as f:
    data = [[i for i in line.rstrip().split(' ')] for line in f]

moves = [Move(d[0], int(d[1])) for d in data]


hor = 0
depth = 0

for m in moves:
    if m.dir == "forward":
        hor = hor + m.val
    if m.dir == "down":
        depth = depth + m.val
    if m.dir == "up":
        depth = depth - m.val

print(f"Part one solution: {hor*depth}")


hor = 0
depth = 0
aim = 0

for m in moves:
    if m.dir == "forward":
        hor = hor + m.val
        depth = depth + aim * m.val
    if m.dir == "down":
        aim = aim + m.val
    if m.dir == "up":
        aim = aim - m.val

print(f"Part two solution: {hor*depth}")