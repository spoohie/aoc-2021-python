def part_one(data):
    outputs = [d[1].split(" ") for d in data]
    flat_outputs = [s for line in outputs for s in line]
    numbers = [len(s) for s in flat_outputs]
    return numbers.count(2) + numbers.count(3) + numbers.count(4) + numbers.count(7)


def part_two(data):
    return sum(calculate_output(d) for d in data)


def calculate_output(line):
    inp, out = line[0].split(" "), line[1].split(" ")
    line = sorted(inp + out, key=len)

    dictionary = [""] * 10
    dictionary = find1478(line, dictionary)
    dictionary = find6(line, dictionary)
    dictionary = find235(line, dictionary)
    dictionary = find0(dictionary)
    dictionary = find9(line, dictionary)

    sorted_out = [sort(s) for s in out]
    return int("".join([str(dictionary.index(s)) for s in sorted_out]))


def find1478(line, dictionary):
    dictionary[1] = sort(next(x for x in line if len(x) == 2))
    dictionary[4] = sort(next(x for x in line if len(x) == 4))
    dictionary[7] = sort(next(x for x in line if len(x) == 3))
    dictionary[8] = sort(next(x for x in line if len(x) == 7))
    return dictionary


def find6(line, dictionary):
    o_1, o_2 = dictionary[1]
    values_len_6 = [x for x in line if len(x) == 6]
    for v in values_len_6:
        if (o_1 in v) ^ (o_2 in v):
            dictionary[6] = sort(v)
            return dictionary


def find235(line, dictionary):
    o_1, o_2 = dictionary[1]
    top_right_side = o_1 if o_1 not in dictionary[6] else o_2
    values_len_5 = [x for x in line if len(x) == 5]
    for v in values_len_5:
        if o_1 in v and o_2 in v:
            dictionary[3] = sort(v)
        elif top_right_side in v:
            dictionary[2] = sort(v)
        else:
            dictionary[5] = sort(v)
    return dictionary


def find0(dictionary):
    eight = dictionary[8]
    o_1, o_2 = dictionary[1]
    top_right_side = o_1 if o_1 not in dictionary[6] else o_2
    common_2_4 = ''.join(set(dictionary[2]).intersection(dictionary[4]))
    middle = common_2_4.replace(top_right_side, "")
    dictionary[0] = eight.replace(middle, "")
    return dictionary


def find9(line, dictionary):
    o_1, o_2 = dictionary[1]
    values_len_6 = [sort(x) for x in line if len(x) == 6]
    for v in values_len_6:
        if v == dictionary[0]:
            pass
        elif o_1 in v and o_2 in v:
            dictionary[9] = sort(v)
            return dictionary


def sort(signal):
    return "".join(sorted(signal))
    

with open('input.txt', 'r') as f:
    data = [line.rstrip().split(" | ") for line in f]

print(f"Part one solution: {part_one(data)}")
print(f"Part one solution: {part_two(data)}")