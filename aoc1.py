import itertools

def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def threes(iterable):
    "s -> (s0,s1,s2), (s1,s2,s3), (s2, s3,4), ..."
    a, b, c = itertools.tee(iterable, 3)
    next(b, None)
    next(c, None)
    next(c, None)
    return zip(a, b, c)

def part_one(data):
    val = 0    

    for a, b in pairwise(data):
        if a < b:
            val = val + 1
    return val


def part_two(data):
    val = 0

    for a, b in pairwise(threes(data)):
        if sum(a) < sum(b):
            val = val + 1
    return val


with open('input.txt', 'r') as f:
    data = [int(i) for i in f] 

print(f"Part one solution: {part_one(data)}")
print(f"Part two solution: {part_two(data)}")