from collections import Counter

def part_one(template, rules):
    for i in range(40):
        template = apply_rules(template, rules)
    lens = Counter(template).values()
    return max(lens) - min(lens)


def apply_rules(template, rules):
    new_formula = ""
    template_pairs = [''.join(pair) for pair in zip(template[:-1], template[1:])]
    if template_pairs[0] in rules:
        new_formula += template_pairs[0][0] + rules[template_pairs[0]] + template_pairs[0][1]
    else:
        new_formula += template_pairs[0]
    for p in template_pairs[1:]:
        if p in rules:
            new_formula += rules[p] + p[1]
        else:
            new_formula += p
    return new_formula


with open('input.txt', 'r') as f:
    template = f.readline().rstrip()
    f.readline() # omit whitespace
    rules = dict(s.rstrip().split(" -> ") for s in f)

print(f"Part one solution: {part_one(template, rules)}")
# print(f"Part two solution: {part_two(data)}")
