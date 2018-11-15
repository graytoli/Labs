# Lab 5: Random Emoticon Generator, attempt 1
import random

eyes = [':', '=', ';', '8']
noses = ['', '^', '-', '{']
mouths = ['3', '(', ')', '\\', '[', ']', '>', '/', 'P', 'p', 'D', 'B', 'o', 'O']

face = random.choice(eyes) + random.choice(noses) + random.choice(mouths)
print(face)
