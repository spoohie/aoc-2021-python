from collections import namedtuple


Ventline = namedtuple('Ventline', 'x1 y1 x2 y2')


def part_one(ventlines, mapsize):
     return calculate_seafloor(ventlines, mapsize, False)


def part_two(ventlines, mapsize):
     return calculate_seafloor(ventlines, mapsize, True)


def calculate_seafloor(ventlines, mapsize, diagonal):
    seafloor = [ [0]*mapsize for _ in range(mapsize) ]

    for v in ventlines:
        if v.x1 == v.x2:
            ys = range(v.y1, v.y2+1) if v.y2 > v.y1 else range(v.y2, v.y1+1)
            for y in ys:
                seafloor[y][v.x1] += 1
        elif v.y1 == v.y2:
            xs = range(v.x1, v.x2+1) if v.x2 > v.x1 else range(v.x2, v.x1+1)
            for x in xs:
                seafloor[v.y1][x] += 1
        elif diagonal:
            if v.x2 > v.x1 and v.y2 > v.y1:
                xs = list(range(v.x1, v.x2+1))
                ys = list(range(v.y1, v.y2+1))
            elif v.x1 > v.x2 and v.y1 > v.y2:
                xs = list(range(v.x2, v.x1+1))
                ys = list(range(v.y2, v.y1+1))
            elif v.x2 > v.x1 and v.y2 < v.y1:
                xs = list(range(v.x1, v.x2+1))
                ys = list(range(v.y1, v.y2-1, -1))
            elif v.x1 > v.x2 and v.y1 < v.y2:
                xs = list(range(v.x1, v.x2-1, -1))
                ys = list(range(v.y1, v.y2+1))
            for x, y in zip(xs, ys):
                seafloor[y][x] += 1
    return sum(1 for line in seafloor for p in line if p > 1)


with open('input.txt', 'r') as f:
    points = [line.rstrip().split(" -> ") for line in f]

ventlines = []
for p in points:
    x1, y1 = p[0].split(",")
    x2, y2 = p[1].split(",")
    ventlines.append(Ventline(int(x1), int(y1), int(x2), int(y2)))


print(f"Part one solution: {part_one(ventlines, 1000)}")
print(f"Part two solution: {part_two(ventlines, 1000)}")