with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

fields = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
]

valid_passports = 0
passport = ""

# Concatentate lines as a passport until empty line reached
for line in lines:
    if line is not "":
        passport += line
        passport += " "
    else:
        valid_passports += sum([(field in passport) for field in fields]) == len(fields)
        passport = ""

valid_passports += sum([(field in passport) for field in fields]) == len(fields)

print(valid_passports)
