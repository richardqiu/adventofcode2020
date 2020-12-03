with open('input.txt', 'r') as f:
    lines = f.readlines()

n_valid_passwords = 0
for line in lines:
    nums, char, password = line.split(" ")
    nums = list(map(int, nums.split("-")))
    char = char.replace(":", "")

    n_valid_chars = 0
    if nums[0] < len(password):
        if password[nums[0]-1] == char:
            n_valid_chars += 1

    if nums[1] < len(password):
        if password[nums[1]-1] == char:
            n_valid_chars += 1

    if (n_valid_chars) % 2 == 1:
        n_valid_passwords += 1

print(n_valid_passwords)

