# Fundamentals: Problem 1
def is_even(a):
    """ returns if number if even
    """
    return a % 2 == 0

num = int(input('Enter a number: ').strip())
even = is_even(num)
if even:
    even = ''
else:
    even = 'not'
print(num, f'is {even} even.')

# Fundamentals: Problem 2
def opposite(a, b):
    """ returns if a and b have opposite polarity
    """
    return (a >= 0 and b < 0) or (a < 0 and b >= 0)

x, y = input('Enter two numbers: ').split()

x = int(x)
y = int(y)
print(x, 'and', y, 'are opposites:', opposite(x, y))

# Dictionaries: Problem 1
def combine(nums1, nums2):
    """ returns combined list of alternating items
    """
    combined = []
    for i in range(len(nums1)):
      combined.append(nums1[i])
      combined.append(nums2[i])
    return combined
    # # equivalent to above
    #while (len(nums1) > 0 and len(nums2) > 0):
    #   combined.append(nums1.pop(0))
    #   combined.append(nums2.pop(0))
    #return combined

print(combine(['a', 'b', 'c'], [1, 2, 3]))

# Strings: Problem 3
alpha = 'abcdefghijklmnopqrstuvwxyz'
def latest_letter(string):
    """ returns letter latest in the English alphabet
    """
    last = string[0]
    for char in string:
        char = char.lower()
        if char.isalpha():
            if char > last:
                last = char
        if last.isalpha():
            return last
        return ''

def max(nums):
    """ returns max of list of nums
    """
    running_max = float('-inf')
    for num in nums:
        if num > running_max:
            running_max = num
    return running_max

def sum(nums):
    """ returns sum of list of numbers
    """
    total = 0
    for num in nums:
        total += num
    return total

# List: Problem 3
def eveneven(nums):
    """ returns true if there are an even amount of even numbers in nums
    """
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(even_num)
    return len(even_nums) % 2 == 0
    # equivalent to above
    even_nums = [num for num in nums if num % 2 == 0]

# Dictionaries: Problem 1
def combine(keys, values):
    t = [(k, v) for k in keys for v in values]
    return t
    # equivalent to above
    combined = {}
    for i in range(len(keys)):
        combined[keys[i]] = values[i]
    return combined
    # equivalent to above
    return dict(zip(keys, values))


def squared(nums):
    # returns list of nums squared
    return [num * num for num in nums]

def even_squares(nums):
    # returns square of num if num is even
    return [num * num for num in nums if num % 2 == 0]

# Dictionaries: Problem 2
combined = {'apple': 1.2, 'banana': 3.3, 'pear': 2.1}

def average(d):
    return sum(d.values()) / len(d)


print(average(combined))


# Lists: Problem 13
def minimum(nums):
    running_min = float('inf')
    for num in nums:
        if num < running_min:
            running_min = num
    return running_min
    # equivalent
    return min(nums)

def maximum(nums):
    running_max = float('-inf')
    for num in nums:
        if num > running_max:
            running_max = num
    return running_max
    # equivalent
    return max(nums)

def mean(nums):
    return sum(nums) / len(nums)

def mode(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    sorted_count = sorted(count.items(), key = lambda kv: kv [1], reverse=True)
    max_count = sorted_count[0][1]
    mode = []
    for item in sorted_count:
        if item[1] == max_count:
            mode.append(item[0])
        else:
            break
    return mode

num_list = [2, 3, 7, 20, -5, 3]
print(minimum(num_list))
print(maximum(num_list))
print(mean(num_list))
print(mode(num_list))


# Comprehensions: Problem 1
powers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def powers_of_two(n_list):
    powers = range(n_list)
    return [2**power for power in powers]

# Comprehensions: Problem 2
def evens(num_list):
    return [num for num in num_list if num % 2 == 0]

print(evens(range(1, 21)))

# Comprehensions: Problem 3
def swap(some_dict):
    return {v:k for k,v in dictionary.items()}

# Recursions: Problem 1
def recursive_summation(n):
    """
    returns sum of all the numbers up to n
    for instance, if n = 4, recursive_summation(4) = 10 = (4 + 3 + 2 + 1)
    >>> recursive_summation(5)
    15
    """
    if n == 0:
        return 0
    return n + recursive_summation(n-1)

print(recursive_summation(1))
