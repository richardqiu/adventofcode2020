with open('input2.txt', 'r') as f:
    nums =  list(map(int, f.read().split()))

summed_pairs = {}

for i, num1 in enumerate(nums):
    for num2 in nums[i+1:]:
        summed_pairs[num1 + num2] = (num1, num2)

for num in nums:
    if 2020 - num in summed_pairs:
        num1, num2 = summed_pairs[2020 - num]
        if num1 == num2 or num == num1 or num == num2:
            print(num1, num2, num)
        else:
            print(num * num1 * num2)
