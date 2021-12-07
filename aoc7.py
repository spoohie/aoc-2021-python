import sys


def part_one(data):
    return calculate_fuel(data, abs)


def part_two(data):
    return calculate_fuel(data, fuel_sum)


def calculate_fuel(data, func):
    fuels = [sum([func(abs(d-i)) for d in data]) for i in range(max(data)+1)]
    return min(fuels)


def fuel_sum(n):
    return int((2+(n-1))*n/2)


with open('input.txt', 'r') as f:
    data = [int(i) for i in f.readline().split(',')]

print(f"Part one solution: {part_one(data)}")
print(f"Part two solution: {part_two(data)}")