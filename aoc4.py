import copy

with open('input.txt', 'r') as f:
    numbers = [int(i) for i in f.readline().strip().split(',')]
    lines = [[int (i) for i in line.strip().split()] for line in f if not line.isspace()]
    data = [lines[x:x+5] for x in range(0, len(lines),5)]

def part_one(numbers, boards):
    for n in numbers:
        draw_number(n, boards)
        for board in boards:
            winner = check_winner(board)
            if winner is not None:
                return n * sum_unmarked(winner)


def draw_number(number, boards):
    for board in boards:
        for line in board:
            for i, elem in enumerate(line):
                if elem == number:
                    line[i] = 'X'


def check_winner(board):
    for line in board:
        if line == ['X','X','X','X','X']:
            return board
    columns = zip(*board)
    for line in columns:
        if list(line) == ['X','X','X','X','X']:
            return board
    return None


def sum_unmarked(board):
    # print(board)
    flat_list = [item for sublist in board for item in sublist]
    nums = [x for x in flat_list if x != 'X']
    return sum(nums)


def part_two(numbers, boards):
    for n in numbers:
        draw_number(n, boards)
        if len(boards) == 1 and check_winner(boards[0]):
            return n * sum_unmarked(boards[0])
        boards = [b for b in boards if not check_winner(b)]


print(f"Part one solution: {part_one(numbers, copy.deepcopy(data))}")
print(f"Part two solution: {part_two(numbers, data)}")