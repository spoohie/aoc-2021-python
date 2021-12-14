from collections import defaultdict
import time


def part_one(template, rules):
    lens = apply_rules(template, rules, 10)
    return max(lens) - min(lens)


def part_two(template, rules):
    lens = apply_rules(template, rules, 40)
    return max(lens) - min(lens)


def apply_rules(template, rules, times):
    lens = defaultdict(int)
    for l in template:
        lens[l] += 1
    pairs = defaultdict(int)
    template_pairs = [''.join(pair) for pair in zip(template[:-1], template[1:])]
    for k in template_pairs:
        pairs[k] += 1
    for _ in range(times):
        new_pairs = defaultdict(int)
        for p in pairs:
            new_pairs[p[0]+rules[p]] += pairs[p]
            new_pairs[rules[p]+p[1]] += pairs[p]
            lens[rules[p]] += pairs[p]
        pairs = new_pairs
    return list(lens.values())
    

start_time = time.time()
with open('input.txt', 'r') as f:
    template = f.readline().rstrip()
    f.readline() # omit empty line
    rules = dict(s.rstrip().split(" -> ") for s in f)

print(f"Part one solution: {part_one(template, rules)}")
print(f"Part two solution: {part_two(template, rules)}")
print("--- %s seconds ---" % (time.time() - start_time))