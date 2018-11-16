# Lab 14: Pick6, version 2
import random

def pick6():
    ticket = []
    for i in range(6):
        ticket.append(random.randint(1, 99))
    return ticket

def matches(winning, purchased):
    num_matches = 0
    for i in range(len(winning)):
        if winning[i] == purchased[i]:
            num_matches += 1
    return num_matches

winning = pick6()
number_of_games = 0
final_balance = 0

while number_of_games < 100000:
    number_of_games +=1
    balance = 0
    purchased = pick6()
    total_matches = matches(winning, purchased)
    if total_matches == 1:
        balance += 4
    elif total_matches == 2:
        balance += 7
    elif total_matches == 3:
        balance += 100
    elif total_matches == 4:
        balance += 50000
    elif total_matches == 5:
        balance += 1000000
    elif total_matches == 6:
        balance += 25000000
    balance -= 2
    final_balance += balance

expenses = number_of_games * 2
ROI = (final_balance - expenses) / expenses
print(f'Your earnings: ${final_balance}')
print(f'Your expenses: ${expenses}')
print(f'ROI: {ROI}')
