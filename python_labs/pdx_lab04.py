# Lab 4: Magic 8-Ball, attempt 1
import random

print("Welcome to Madame Lenormand's Crystal Ballroom...")

prompt = input("Ask Madame Lenormand a question: ")

predictions = ['It is certain.', 'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Reply hazy. Try again.', 'Better not tell you now.', 'Don\'t count on it.', 'My sources say no.']

print(random.choice(predictions))