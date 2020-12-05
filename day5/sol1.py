# Richard Qiu
# Advent of Code 2020, Day 5

def main():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    highest_id = 0
    for line in lines:
        highest_id = max(pass_to_id(line), highest_id)

    print(highest_id)


def pass_to_id(boarding_pass):
    row = boarding_pass[:7]
    seat = boarding_pass[8:]
    row = int(row.replace("B", "1").replace("F", "0"), 2)
    seat = int(seat.replace("R", "1").replace("L", "0"), 2)
    return row * 8 + seat


if __name__ == "__main__":
    main()
