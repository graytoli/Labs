# Lab 14: Pick6, version 1
import random

def pick6():
    ticket = []
    for i in range(6):
        ticket.append(random.randint(1, 99))
    return ticket

def matches(winning, purchased):
    num_matches = 0
    for num in winning:
        num_idx = winning.index(num)
        if purchased[num_idx] == num:
            num_matches += 1
    return num_matches

number_of_games = 0
final_balance = 0

while number_of_games < 100000:
    number_of_games +=1
    balance = 0
    winning = pick6()
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

print(f'Your final balance is: ${final_balance}')
