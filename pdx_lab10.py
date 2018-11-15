# Lab 10: Average Numbers, version 1
nums = [5, 0, 8, 3, 4, 1, 6]
sum = 0

for num in nums:
    print(num)
    sum = sum + num

average = sum / len(nums)
print(f'The average of these numbers is: {average}')
