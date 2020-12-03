with open('input.txt', 'r') as f:
    lines = f.readlines()

n_valid_passwords = 0
for line in lines:
    nums, char, password = line.split(" ")
    nums = list(map(int, nums.split("-")))
    char = char.replace(":", "")
    if nums[0] <= password.count(char) <= nums[1]:
        n_valid_passwords += 1

print(n_valid_passwords)

