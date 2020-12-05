# Richard Qiu
# Advent of Code 2020, Day 5

def main():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    ids_on_flight = []
    for line in lines:
        ids_on_flight.append(pass_to_id(line))
    ids_on_flight.sort()

    last_id = ids_on_flight[0] - 1
    for id_on_flight in ids_on_flight:
        if id_on_flight != last_id + 1:
            print(id_on_flight - 1)
            break
        last_id = id_on_flight


def pass_to_id(boarding_pass):
    row = boarding_pass[:7]
    seat = boarding_pass[7:]
    row = int(row.replace("B", "1").replace("F", "0"), 2)
    seat = int(seat.replace("R", "1").replace("L", "0"), 2)
    return row * 8 + seat


if __name__ == "__main__":
    main()
