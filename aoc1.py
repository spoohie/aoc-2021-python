import itertools


with open('input.txt', 'r') as f:
    data = [int(i) for i in f] 


def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)   


val = 0    

for a, b in pairwise(data):
    if a < b:
        val = val + 1

print(f"Part one solution: {val}")


def threes(iterator):
    "s -> (s0,s1,s2), (s1,s2,s3), (s2, s3,4), ..."
    a, b, c = itertools.tee(iterator, 3)
    next(b, None)
    next(c, None)
    next(c, None)
    return zip(a, b, c)


val = 0

for a, b in pairwise(threes(data)):
    if sum(a) < sum(b):
        val = val + 1

print(f"Part two solution: {val}")