# Lab 10: Average Numbers, version 2
nums = []
sum = 0

while True:
    user_input = input('Enter a number, or type \'done\': ').strip().lower()
    if user_input == 'done':
        break
    nums.append(int(user_input))
    sum = sum + int(user_input)

if sum != 0:
    average = sum / len(nums)
    print(f'The average of these numbers is: {average}')
else:
    print('Exiting program...')
