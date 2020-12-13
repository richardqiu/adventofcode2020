# Richard Qiu
# Advent of Code 2020, Day 13

from math import prod


def main():

    with open("input.txt", "r") as f:
        __, buses = f.read().splitlines()

    buses = [(int(bus), i) for i, bus in enumerate(buses.split(",")) if bus != "x"]
    buses = [(bus, bus - i % bus) for bus, i in buses]

    check_interval, n = buses[0]
    if n == 0:
        n += check_interval
    for bus, remainder in buses[1:]:
        print(bus, remainder, n)
        while True:
            if n % bus == remainder:
                check_interval *= bus
                break
            else:
                n += check_interval
    return n


if __name__ == "__main__":
    print(main())
