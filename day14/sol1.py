# Richard Qiu
# Advent of Code 2020, Day 14

from collections import defaultdict


def main():
    with open("input.txt", "r") as f:
        lines = [line.split(" = ") for line in f.read().splitlines()]

    bitmask = lines[0][1]
    mem = defaultdict(int)
    for command, data in lines[1:]:
        if command == "mask":
            bitmask = data
        else:
            address = int(command[4:-1])
            masked_data = apply_bitmask(bitmask, int(data))
            mem[address] = masked_data

    return sum(masked_data for masked_data in mem.values())


def apply_bitmask(bitmask, data):
    data = bin(data)[2:]
    data = list("0" * (36 - len(data)) + data)
    for i, mask in enumerate(bitmask):
        if mask == "X":
            pass
        else:
            data[i] = mask
    return int("".join(data), 2)


if __name__ == "__main__":
    print(main())
