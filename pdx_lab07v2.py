# Lab 7: Rock Paper Scissors, attempt 2
import random

print("Let's play Rock Paper Scissors! Choose wisely.")

while True:
    user_choice = input("Rock, paper, or scissors? ").strip().lower()
    options = ['rock', 'paper', 'scissors']
    comp_choice = random.choice(options)
    match = user_choice + ' vs. ' + comp_choice
    print(match)

    if match in ['rock vs. rock', 'paper vs. paper', 'scissor vs. scissors']:
        print('Tie!')
    elif match in ['rock vs. scissors', 'paper vs. rock', 'scissors vs. paper']:
        print('You won!')
    else:
        print('You lost...Maybe next time...')
    while True:
        play_again = input('Wanna play again? ').strip().lower()
        if play_again in ['yes', 'y', 'no', 'n', 'sure', 'nope']:
            break
    if play_again in ['no', 'n', 'nope']:
        break
