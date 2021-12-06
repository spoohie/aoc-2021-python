def part_one(data):
    return calculate_growth(data, 80)


def part_two(data):
    return calculate_growth(data, 256)


def calculate_growth(data, days):
    fish_by_age = [0] * 9
    for f in data:
        fish_by_age[f] += 1

    for _ in range(days):
        zeroes = 0
        for i, f in enumerate(fish_by_age):
            if i == 0 and f > 0:
                zeroes = f
            else:
                fish_by_age[i-1] += f
            fish_by_age[i] = 0
        fish_by_age[6] += zeroes
        fish_by_age[8] += zeroes
    return sum(fish_by_age)


with open('input.txt', 'r') as f:
    data = [int(i) for i in f.readline().split(',')]

print(f"Part one solution: {part_one(data)}")
print(f"Part two solution: {part_two(data)}")