with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]

width = len(lines[0])
trees_product = 1
for over, down in slopes:
    x = 0
    trees = 0
    for line in lines[::down]:
        if line[x] == "#":
            trees += 1
        x = (x + over) % width

    trees_product *= trees

print(trees_product)
