# Lab 6: Password Generator, version 1
import random

n = 0
letter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
list = []

while n <= 12:
    n += 1
    character = random.choice(letter) + str(random.randint(0, 9))
# Idea provided by responder at https://stackoverflow.com/questions/2475518/python-how-to-append-elements-to-a-list-randomly
    list.insert(random.randint(0, len(list)), random.choice(character))

print(f"Your new password: {''.join(list)}")
