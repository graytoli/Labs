# Lab 4: Magic 8-Ball, version 2
import random

print("Welcome to Madame Lenormand's Crystal Ballroom...")

predictions = ['It is certain.', 'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Reply hazy. Try again.', 'Better not tell you now.', 'Don\'t count on it.', 'My sources say no.']

while True:
    user_input = input("Ask Madame Lenormand a question: ").strip().lower()
    if user_input == 'done':
        break
    print(random.choice(predictions))
