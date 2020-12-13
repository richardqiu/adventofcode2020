# Richard Qiu
# Advent of Code 2020, Day 12


def main():
    waypt_coords = [10, 1]
    ship_coords = [0, 0]

    with open("input.txt", "r") as f:
        lines = [(line[0], int(line[1:])) for line in f.read().splitlines()]

    for direction, num in lines:
        if direction == "L":
            for i in range(num // 90):
                waypt_coords[0], waypt_coords[1] = -waypt_coords[1], waypt_coords[0]
        elif direction == "R":
            for i in range(num // 90):
                waypt_coords[0], waypt_coords[1] = waypt_coords[1], -waypt_coords[0] elif direction == "N":
            waypt_coords[1] += num
        elif direction == "S":
            waypt_coords[1] -= num
        elif direction == "E":
            waypt_coords[0] += num
        elif direction == "W":
            waypt_coords[0] -= num
        else:
            ship_coords[0] += num * waypt_coords[0]
            ship_coords[1] += num * waypt_coords[1]

    return abs(ship_coords[0]) + abs(ship_coords[1])


if __name__ == "__main__":
    print(main())
