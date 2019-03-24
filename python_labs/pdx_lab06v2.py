# Lab 6: Password Generator, version 2
import random

n = 0
letter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
list = []

pw_length = int(input('How many characters do you want in your password? ').strip())

while n <= pw_length:
    n += 1
    character = random.choice(letter) + str(random.randint(0, 9))
# Idea provided by responder at https://stackoverflow.com/questions/2475518/python-how-to-append-elements-to-a-list-randomly
    list.insert(random.randint(0, len(list)), random.choice(character))

print(f"Your new password: {''.join(list)}")
