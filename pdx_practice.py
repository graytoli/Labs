# def is_even(a):
#   return a%2 == 0
#
# num = int(input('Enter a number: ').strip())
# even = is_even(num)
# if even:
#     even = ''
# else:
#     even = 'not'
# print(num, f'is {even} even.')
#
#
# def opposite(a, b):
#     return (a >= 0 and b < 0) or (a < 0 and b >= 0)
#
# x, y = input('Enter two numbers: ').split()
#
# x = int(x)
# y = int(y)
# print(x, 'and', y, 'are opposites:', opposite(x, y))
#
#
# def combine(nums1, nums2):
#     combined = []
#     for i in range(len(nums1)):
#       combined.append(nums1[i])
#       combined.append(nums2[i])
#     return combined
# print(combine(['a', 'b', 'c'], [1, 2 , 3]))
alpha = 'abcdefghijklmnopqrstuvwxyz'

def latest_letter(string):
    list = string.split()
    for letter in list:
        match = alpha.find(letter)
        if match > -1:
