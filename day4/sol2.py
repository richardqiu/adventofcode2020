# Richard Qiu
# Advent of Code 2020, Day 4

import re

# name, low, high of various passport fields
numerical_fields = [
    ["byr", 1920, 2002],
    ["iyr", 2010, 2020],
    ["eyr", 2020, 2030],
]

# List of valid eye colors
eye_colors = [
    "amb",
    "blu",
    "brn",
    "gry",
    "grn",
    "hzl",
    "oth",
]


def main():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    valid_passports = 0
    passport = ""

    # Concatentate lines as a passport until empty line reached
    for line in lines:
        if line is not "":
            passport += line
            passport += " "
        else:
            valid_passports += is_passport_valid(passport)
            passport = ""

    valid_passports += is_passport_valid(passport)

    print(valid_passports)


def is_passport_valid(passport):
    # Check byr, iyr, eyr
    for numerical_field, low, high in numerical_fields:
        try:
            regex = f"(?<={numerical_field}:)[0-9]+"
            if low <= int(re.search(regex, passport).group()) <= high:
                pass
            else:
                return False
        except:
            return False

    # Check hgt
    try:
        hgt = re.search("(?<=hgt:)[0-9]{2,3}(cm|in)", passport).group()
        if hgt[-2:] == "cm" and (150 <= int(hgt[:-2]) <= 193):
            pass
        elif hgt[-2:] == "in" and (59 <= int(hgt[:-2]) <= 76):
            pass
        else:
            return False
    except:
        return False

    # Check hcl
    try:
        if len(re.search("(?<=hcl:)#[0-9a-f]+", passport).group()) == 7:
            pass
        else:
            return False
    except:
        return False

    #  Check ecl
    try:
        eye_color = re.search("(?<=ecl:)[a-z]+", passport).group()
        if eye_color in eye_colors:
            pass
        else:
            return False
    except:
        return False

    # Check pid
    try:
        if len(re.search("(?<=pid:)[0-9]+", passport).group()) == 9:
            pass
        else:
            return False
    except:
        return False

    return True


if __name__ == "__main__":
    main()
