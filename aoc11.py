import copy
from itertools import product


def part_one(data):
    return sum(step(data) for _ in range(100))
        

def step(data):
    flashes = 0
    data = increment_data(data)
    for k, v in data.items():
        if v > 9:
            flashes += flash(k, find_neighbours(k, data), data)
    return flashes


def increment_data(data):
    for node in data:
        data[node] += 1
    return data


def find_neighbours(node, data):
    return [n for n in [(node[0]-1, node[1]-1), (node[0], node[1]-1), (node[0]+1, node[1]-1),
                        (node[0]-1, node[1]),                         (node[0]+1, node[1]),
                        (node[0]-1, node[1]+1), (node[0], node[1]+1), (node[0]+1, node[1]+1)] if n in data]


def flash(node, neighbours, data, flashes=0):
    flashes += 1
    data[node] = 0
    for n in neighbours:
        if data[n] == 0:
            continue
        data[n] += 1
        if data[n] > 9:
            flashes = flash(n, find_neighbours(n, data), data, flashes)
    return flashes


def part_two(data):
    steps = 0
    while step(data) != len(data):
        steps += 1
    return steps+1


with open('input.txt', 'r') as f:
    data = [list(map(int, list(i.rstrip()))) for i in f]

carthesian_product = list(product(range(len(data[0])), range(len(data))))
octo = { key: data[key[1]][key[0]] for key in carthesian_product }

print(f"Part one solution: {part_one(copy.deepcopy(octo))}")
print(f"Part two solution: {part_two(octo)}")