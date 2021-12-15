from itertools import product
import networkx as nx
import matplotlib.pyplot as plt


def part_one(risks):
    g = nx.DiGraph()
    for r in risks:
        neighbours = find_neighbours(r, risks)
        # print(f"r:{r}, v:{risks[r]}, neigh:{neighbours}")
        for n in neighbours:
            # if not g.has_edge(r, n):
            g.add_edge(r, n, weight=risks[n])
            g.add_edge(n, r, weight=risks[r])
    path = nx.shortest_path(g, source=(0,0), target=(99,99), weight='weight')
    return sum(risks[p] for p in path[1:])
    # return paths+risks[(99,99)]
    # for e in g.edges().data():
    #     print(e)
    # for p in paths:
    #     print(p)
        # print(list(risks[tuple(path)] for path in p)[1:])
        # print(sum(list(risks[tuple(path)] for path in p)[1:]))
    # return sum(weights)
            


def find_neighbours(node, data):
    return [n for n in [(node[0], node[1]-1),
                        (node[0]-1, node[1]), (node[0]+1, node[1]),
                        (node[0], node[1]+1)] if n in data]


with open('input.txt', 'r') as f:
    data = [list(map(int, list(i.rstrip()))) for i in f]

carthesian_product = list(product(range(len(data[0])), range(len(data))))
risks = { key: data[key[1]][key[0]] for key in carthesian_product }

print(f"Part one solution: {part_one(risks)}")