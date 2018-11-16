# Lab 19: Blackjack Advice, version 1

def main():
    cards = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
    while True:
        first = cards.get(input('What\'s your first card? ').upper(), 0)
        second = cards.get(input('What\'s your second card? ').upper(), 0)
        third = cards.get(input('What\'s your third card? ').upper(), 0)
        if 0 not in [first, second, third]:
            break
        else:
            print('One of the cards entered does not exist. Try again.')
    points = first + second + third
    return points

def advice(points):
    if points < 17:
        print(f'{points} Hit')
    elif points == 21:
        print(f'{points} Blackjack!')
    elif points > 21:
        print(f'{points} Already Busted')
    else:
        print(f'{points} Stay')

advice(main())
