with open('input.txt', 'r') as f:
    nums =  list(map(int, f.read().split()))

s = set()
for num in nums:
    if num in s:
        print(num * (2020 - num))
    else:
        s.add(2020 - num)
