import math


class Packet:
    def __init__(self, data):
        self.version, data = self.__read(data, 3)
        self.typeId, data = self.__read(data, 3)
        self.length, data = self.__read(data, 1) if self.typeId != 4 else (None, data)
        self.body = []

        if self.typeId == 4:
            self.literal, self.tail = self.__read_literal(data)
        else:
            self.tail = self.__read_subpackets(data)

    def __read(self, data, bits):
        return int(data[:bits], 2), data[bits:]

    def __read_literal(self, data):
        literal = ""
        while True:
            literal += data[1:5]
            if data[0] == "0":
                return int(literal, 2), data[5:]
            data = data[5:]

    def __read_subpackets(self, data):
        if self.length == 0:
            return self.__read_subpackets_by_length(data)
        else:
            return self.__read_subpackets_by_number(data)

    def __read_subpackets_by_length(self, data):
        length, data = int(data[:15], 2), data[15:]
        subpackets_data, data = data[:length], data[length:]
        while subpackets_data:
            p = Packet(subpackets_data)
            self.body.append(p)
            subpackets_data = p.get_tail()
        return data

    def __read_subpackets_by_number(self, data):
        num, data = int(data[:11], 2), data[11:]
        for _ in range(num):
            p = Packet(data)
            self.body.append(p)
            data = p.get_tail()
        return data

    def value(self):
        values = [p.value() for p in self.body]
        if self.typeId == 4:
            return self.literal
        if self.typeId == 0:
            return sum(values)
        if self.typeId == 1:
            return math.prod(values)
        if self.typeId == 2:
            return min(values)
        if self.typeId == 3:
            return max(values)
        if self.typeId == 5:
            return 1 if values[0] > values[1] else 0
        if self.typeId == 6:
            return 1 if values[0] < values[1] else 0
        if self.typeId == 7:
            return 1 if values[0] == values[1] else 0

    def get_tail(self):
        return self.tail

    def version_sum(self):
        return self.version + sum(p.version_sum() for p in self.body)


def hextobin(data):
    integer = int(data, 16)
    return f'{integer:0>{len(data)*4}b}'


def part_one(data):
    p = Packet(data)
    return p.version_sum()

def part_two(data):
    p = Packet(data)
    return p.value()


with open('input.txt', 'r') as f:
    data = f.readline().rstrip()
data = hextobin(data)

print(f"Part one solution: {part_one(data)}")
print(f"Part two solution: {part_two(data)}")