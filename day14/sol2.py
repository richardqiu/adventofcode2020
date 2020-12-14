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
            masked_addresses = apply_bitmask(bitmask, address)
            for masked_address in masked_addresses:
                mem[masked_address] = int(data)

    return sum(masked_data for masked_data in mem.values())


def apply_bitmask(bitmask, address):
    address = bin(address)[2:]
    address = list("0" * (36 - len(address)) + address)
    for i, mask in enumerate(bitmask):
        if mask == "0":
            pass
        else:
            address[i] = mask
    return [int(address, 2) for address in subroutine(bitmask, "".join(address))]


def subroutine(bitmask, address):
    if (index := bitmask.find("X")) == -1:
        return [address]
    else:
        addresses = []
        bitmask = bitmask.replace("X", "0", 1)
        for sub in ["0", "1"]:
            substituted_address = address[:index] + sub + address[index + 1 :]
            addresses.extend(bitmask_subroutine(bitmask, substituted_address))
        return addresses


if __name__ == "__main__":
    print(main())
