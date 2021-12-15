from itertools import product
import networkx as nx


def part_one(data):
    risks, start, end = build_risks_map(data)
    return find_path_length(risks, start, end)


def part_two(data):
    data = extend_risks_data(data)
    risks, start, end = build_risks_map(data)
    return find_path_length(risks, start, end)


def build_risks_map(data):
    carthesian_product = list(product(range(len(data[0])), range(len(data))))
    risks = { key: data[key[1]][key[0]] for key in carthesian_product }
    return risks, carthesian_product[0], carthesian_product[-1]


def find_path_length(graph, start, end):
    g = nx.DiGraph()
    for r in graph:
        neighbours = find_neighbours(r, graph)
        for n in neighbours:
            g.add_edge(r, n, weight=graph[n])
            g.add_edge(n, r, weight=graph[r])
    path = nx.shortest_path(g, start, end, weight='weight')
    return sum(graph[p] for p in path[1:])


def find_neighbours(node, data):
    return [n for n in [(node[0], node[1]-1),
                        (node[0]-1, node[1]), (node[0]+1, node[1]),
                        (node[0], node[1]+1)] if n in data]


def extend_risks_data(data):
    size = len(data)
    new_data = []
    for row in data:
        temp_row = []
        temp_row.extend(row)
        for i in range(size, 5 * size):
            temp_row.append(temp_row[i - size] % 9 + 1)
        new_data.append(temp_row)
    for i in range(size, 5 * size):
        new_data.append([i % 9 + 1 for i in new_data[i - size]])
    return new_data


with open('input.txt', 'r') as f:
    data = [list(map(int, list(i.rstrip()))) for i in f]

print(f"Part one solution: {part_one(data)}")
print(f"Part one solution: {part_two(data)}")