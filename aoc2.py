with open('input.txt', 'r') as f:
    data = [[i for i in line.rstrip().split(' ')] for line in f]

hor = 0
depth = 0

for d in data:
    if d[0] == "forward":
        hor = hor + int(d[1])
    if d[0] == "down":
        depth = depth + int(d[1])
    if d[0] == "up":
        depth = depth - int(d[1])

print(f"Part one solution: {hor*depth}")

hor = 0
depth = 0
aim = 0

for d in data:
    if d[0] == "forward":
        hor = hor + int(d[1])
        depth = depth + (aim * int(d[1]))
    if d[0] == "down":
        aim = aim + int(d[1])
    if d[0] == "up":
        aim = aim - int(d[1])

print(f"Part two solution: {hor*depth}")