import copy


def part_one(data, folds):
    data = fold(data, folds)
    return sum(1 for line in data for p in line if p == '#')


def fold(data, folds):
    for f in folds:
        if f[0] == 'x':
            data = fold_horizontally(data, f[1])
        if f[0] == 'y':
            data = fold_vertically(data, f[1])
    return data


def fold_horizontally(data, index):
    for i, d in enumerate(data):
        data[i] = fold_line(d, index)
    return data


def fold_line(line, index):
    l, r = line[:index], line[index+1:]
    return [sum_points(x, y) for x, y in list(zip(l, r[::-1]))]


def sum_points(p1, p2):
    return '.' if p1 == '.' and p2 == '.' else '#'


def fold_vertically(data, index):
    flipped_data = list(zip(*data))
    flipped_data = fold_horizontally(flipped_data, index)
    return list(zip(*flipped_data))


def part_two(data, folds):
    data = fold(data, folds)
    for d in data:
        print(d)


with open('input.txt', 'r') as f:
    coords = list() 
    for s in f:
        if s == "\n":
            break
        coords.append(tuple(map(int, s.rstrip().split(','))))
    folds = [s.rstrip().split(' ')[2].split('=') for s in f]

folds = [(f[0], int(f[1])) for f in folds]
by_coord = list(zip(*coords))
max_x, max_y = max(by_coord[0]), max(by_coord[1])

paper = [['.' for x in range(max_x+1)] for y in range(max_y+1)]
for p in coords:
    paper[p[1]][p[0]]="#"


print(f"Part one solution: {part_one(copy.deepcopy(paper), [folds[0]])}")
print(f"Part two solution: {part_two(paper, folds)}")