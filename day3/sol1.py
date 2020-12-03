with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

x = 0
width = len(lines[0])
trees = 0

for line in lines:
    if line[x] == "#":
        trees += 1
    x = (x + 3) % width

print(trees)
