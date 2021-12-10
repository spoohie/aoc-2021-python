def part_one(data):
    illegal = list()
    for line in data:
        if i := find_corrupted(line):
            illegal.append(i) 

    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    return sum(points[i] for i in illegal)


def find_corrupted(line):
    rev_brackets = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
    }

    stack = list()
    for c in line:
        if c in rev_brackets.keys():
            if stack.pop() != rev_brackets[c]:
                return c
        else:
            stack.append(c)


def part_two(data):
    data = [l for l in data if not find_corrupted(l)]
    closures = [find_closure(line) for line in data]
    scores = sorted([score(c) for c in closures])
    middle_index = int((len(scores)-1)/2)
    return scores[middle_index]


def find_closure(line):
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    closing_brackets = list()
    for c in line:
        if c in brackets.keys():
            closing_brackets.insert(0, brackets[c])
        else:
            if closing_brackets[0] == c:
                closing_brackets.pop(0)
    return closing_brackets


def score(closure):
    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    score = 0
    for c in closure:
        score *= 5
        score += points[c]
    return score


with open('input.txt', 'r') as f:
    data = [s.rstrip() for s in f]

print(f"Part one solution: {part_one(data)}")
print(f"Part two solution: {part_two(data)}")