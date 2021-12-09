def part_one(data):
    lowest = list()
    for y, line in enumerate(data):
        for x, v in enumerate(line):
            l=r=u=d=10
            if x > 0:
                l = int(line[x-1])
            if x < len(line)-1:
                r = int(line[x+1])
            if y > 0:
                u = int(data[y-1][x])
            if y < len(data)-1:
                d = int(data[y+1][x])
            v = int(v)
            if v < l and v < r and v < u and v < d:
                lowest.append(v+1)
    return sum(lowest)


with open('input.txt', 'r') as f:
    data = [i.rstrip() for i in f]

print(f"Part one solution: {part_one(data)}")
# print(f"Part two solution: {part_two(data)}")