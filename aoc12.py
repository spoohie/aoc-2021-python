from collections import Counter, defaultdict


def part_one(paths):
    return find_paths(paths)


def condition_part_one(node, path):
    return not (node.islower() and node in path)


def find_paths(paths, node='start', path=[], count=0, can_put_node=condition_part_one):
    if not can_put_node(node, path):
        return 0
    path.append(node)
    if node == 'end':
        return 1
    for n in paths[node]:
        if not can_put_node(n, path):
            continue
        count += find_paths(paths, n, path[:], can_put_node=can_put_node)
    return count


def part_two(paths):
    return find_paths(paths, path=[], can_put_node=condition_part_two)


def condition_part_two(node, path):
    if node == 'start' or node == 'end':
        if node in path:
            return False
    if node.islower() and node in path and path_contains_lower_pair(path):
        return False
    return True


def path_contains_lower_pair(path):
    c = dict(Counter(path))
    for k, v in c.items():
        if k.islower() and v == 2:
            return True
    return False


with open('input.txt', 'r') as f:
    data = [tuple(i.strip().split('-')) for i in f]
adjacency_list = defaultdict(list)
for src, dest in data:
    adjacency_list[src].append(dest)
    adjacency_list[dest].append(src)


print(f"Part one solution: {part_one(adjacency_list)}")
print(f"Part two solution: {part_two(adjacency_list)}")