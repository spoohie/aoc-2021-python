from itertools import product


def part_one(depths):
    lowest = lowest_points(depths)
    return sum(depths[l]+1 for l in lowest)


def lowest_points(depths):
    lowest_points = list()
    for node, depth in depths.items():
        neigbour_depths = [depths[n] for n in find_neighbours(node, depths)]
        if all(v > depth for v in neigbour_depths):
            lowest_points.append(node)
    return lowest_points


def find_neighbours(node, depths):
    return [k for k in [(node[0]-1, node[1]), (node[0]+1, node[1]), (node[0], node[1]-1), (node[0], node[1]+1)] if k in depths]


def part_two(depths):
    lowest = lowest_points(depths)
    basin_sizes = sorted([find_basin_size(node, depths) for node in lowest], reverse=True)
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


def find_basin_size(node, depths):
    basin = { key: False for key in depths.keys() }
    _, size = dfs(depths, node, basin)
    return size


def dfs(depths, node, basin, size=0):
    if not basin[node]:
        basin[node] = True
        if depths[node] < 9:
            size += 1
            neigbours = find_neighbours(node, depths)
            for n in neigbours:
                basin, size = dfs(depths, n, basin, size)
    return basin, size


with open('input.txt', 'r') as f:
    data = [list(map(int, list(i.rstrip()))) for i in f]

carthesian_product = list(product(range(len(data[0])), range(len(data))))
depths = { key: data[key[1]][key[0]] for key in carthesian_product }

print(f"Part one solution: {part_one(depths)}")
print(f"Part two solution: {part_two(depths)}")