def part_one(data):
    gamma, epsilon = calculate_bit_chains(data)
    return int(gamma, 2) * int(epsilon, 2)


def calculate_bit_chains(data):
    mcb = ""
    lcb = ""
    for i in range(LEN):
        s = [d[i] for d in data]
        mcb = mcb + most_common(s)
        lcb = lcb + least_common(s)
    return mcb, lcb


def most_common(s):
    return '1' if s.count('1') >= s.count('0') else '0'


def least_common(s):
    return '0' if s.count('1') >= s.count('0') else '1'


def part_two(data):
    return oxygen_rating(data[:]) * co2_rating(data[:])


def oxygen_rating(data):
    for i in range(LEN):
        mcb_chain, _ = calculate_bit_chains(data)
        data = [d for d in data if d[i] == mcb_chain[i]]
        if len(data) == 1:
            return int(data[0], 2)


def co2_rating(data):
    for i in range(LEN):
        _, lcb_chain = calculate_bit_chains(data)
        data = [d for d in data if d[i] == lcb_chain[i]]
        if len(data) == 1:
            return int(data[0], 2)


with open('input.txt', 'r') as f:
    data = [i.strip() for i in f]
    LEN = len(data[0])

print(f"Part one solution: {part_one(data)}")
print(f"Part two solution: {part_two(data)}")