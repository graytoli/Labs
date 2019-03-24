# Lab 17: Palindrome and Anagram, version 1
def check_palindrome(user_input):
    char_list = list(user_input.lower())
    char_reversed = list(reversed(char_list))
    if char_list == char_reversed:
        print(f'{user_input} is a palindrome!')
    else:
        print(f'{user_input} is not a palindrome.')

user_input = input('Discover if a word is a palindrome!\nType in a word:\n').strip()
check_palindrome(user_input)


def check_anagram(first_word, second_word):
    first = sorted(first_word.lower().replace(' ',''))
    second = sorted(second_word.lower().replace(' ', ''))
    if first == second:
        print(f'{first_word} and {second_word} are anagrams!')
    else:
        print(f'{first_word} and {second_word} are not anagrams...')

print('Determine if two words are anagrams of each other!')
first_word = input('Enter the first word: ').strip()
second_word = input('Enter the second word: ').strip()
check_anagram(first_word, second_word)
