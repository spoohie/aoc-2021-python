from collections import namedtuple


Move = namedtuple('Move', 'dir val')


def part_one(moves):
    hor = 0
    depth = 0

    for m in moves:
        if m.dir == "forward":
            hor = hor + m.val
        if m.dir == "down":
            depth = depth + m.val
        if m.dir == "up":
            depth = depth - m.val
    return hor*depth


def part_two(moves):
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
    return hor*depth


with open('input.txt', 'r') as f:
    for line in f:
        data = [[i for i in line.rstrip().split(' ')] for line in f]

moves = [Move(d[0], int(d[1])) for d in data]

print(f"Part one solution: {part_one(moves)}")
print(f"Part two solution: {part_two(moves)}")