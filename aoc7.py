import sys


def part_one(data):
    return calculate_fuel(data, abs)


def part_two(data):
    return calculate_fuel(data, fuel_sum)


def calculate_fuel(data, func):
    current_fuel = sys.maxsize
    for i in range(max(data)+1):
        new_fuel = sum([func(d-i) for d in data])
        if new_fuel < current_fuel:
            current_fuel = new_fuel
    return current_fuel


def fuel_sum(diff):
    n = abs(diff)
    return int((2+(n-1))*n/2)


with open('input.txt', 'r') as f:
    data = [int(i) for i in f.readline().split(',')]

print(f"Part one solution: {part_one(data)}")
print(f"Part two solution: {part_two(data)}")