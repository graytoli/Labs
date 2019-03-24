# Card Deck
import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f'Card({self.rank}, {self.suit})'

class Deck:
    def __init__(self):
        ranks = list('A23456789') + ['10'] + list('JQK')
        suits = ['clubs', 'diamonds', 'hearts', 'spades']
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]
## same as above
        # self.cards = []
        # for suit in suits:
        #     for rank in ranks:
        #         card = Card(rank, suit)
        #         self.cards.append(card)

    def __str__(self):
        return str(self.cards)

    def __getitem__(self, idx):
        return self.cards[idx]

    def __len__(self):
        return len(self.cards)

    def draw(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)

    def cut(self):
        index = random.randint(0, len(self.cards) - 1)
        bottom = self.cards[:index]
        top = self.cards[index:]
        self.cards = top + bottom

if __name__ == '__main__':
    deck = Deck()
    print(deck.cards)
    print(deck[0])
    print(deck[-1])
    print(deck.draw())
    print(len(deck))
    print(deck)
    deck.shuffle()
    print(deck)
    deck.cut()
