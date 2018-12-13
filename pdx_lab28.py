# Lab 28: Tic-Tac-Toe
from collections import namedtuple

Player = namedtuple('Player', ['name', 'token'])

class Board:
    def __init__(self):
        self.board = [str(num) for num in range(1, 10)]

    def __repr__(self):
        board = ''
        for i in range(0, 7, 3):
            board += '|'.join([self.board[i], self.board[i+1], self.board[i+2]])
            board += '\n'
        return board

    def position_open(self, index):
        if self.board[index] in ['X', 'O']:
            return False
        return True

    def move(self, position, token):
        index = position - 1
        if self.position_open(index):
            self.board[index] = token
            return False
        if self.is_game_over():
            return False
        return 'That position is occupied.'

    def calc_winner(self):
        for i in range(0, 7, 3):
            if self.board[i] in ['X', 'O']:
                # horizontal matches
                a = self.board[i]
                b = self.board[i+1]
                c = self.board[i+2]

                if a == b == c:
                    return self.board[i]

        for i in range(3):
            if self.board[i] in ['X', 'O']:
                # vertical matches
                a = self.board[i]
                b = self.board[i+3]
                c = self.board[i+6]

                if a == b == c:
                    return self.board[i]

        if self.board[4] in ['X', 'O']:
            if self.board[0] == self.board[4] and self.board[4] == self.board[8]:
                return self.board[1]
            if self.board[2] == self.board[4] and self.board[4] == self.board[6]:
                return self.board[2]

        return None


    def is_full(self):
        for i in range(10):
            if self.board[i] not in ['X', 'O']:
                return False
        return True

    def is_game_over(self):
        if self.calc_winner() or self.is_full():
            return True
        return False


if __name__ == '__main__':
    print("Let's play Tic-Tac-Toe!")
    while True:
        while True:
            board = Board()
            player1_name = input("Enter 1st player's name: ").strip()
            player1_tok = input('Choose X or O: ').strip().upper()
            if player1_tok in ['X', 'O']:
                player_one = Player(player1_name, player1_tok)
                player2_name = input("Enter 2nd player's name: ").strip()
                if player1_tok == 'X':
                    player2_tok = 'O'
                else:
                    player2_tok = 'X'
                player_two = Player(player2_name, player2_tok)
                print(f'{player1_name} is {player1_tok}.\n{player2_name} is {player2_tok}.')
                print('X makes the first move.')

                while True:
                    print(board)

                    if player1_tok == 'X':
                        while True:
                            position = int(input(f'{player1_name}:\nEnter a position on the board to play: '))
                            current_move = board.move(position, player1_tok)
                            if current_move:
                                print(current_move)
                            else:
                                break

                        while True:
                            position = int(input(f'{player2_name}:\nEnter a position on the board to play: '))
                            current_move = board.move(position, player2_tok)
                            if current_move:
                                print(current_move)
                            else:
                                break

                    if player2_tok == 'X':
                        while True:
                            position = int(input(f'{player2_name}:\nEnter a position on the board to play: '))
                            current_move = board.move(position, player2_tok)
                            if current_move:
                                print(current_move)
                            else:
                                break

                        while True:
                            position = int(input(f'{player1_name}:\nEnter a position on the board to play: '))
                            current_move = board.move(position, player1_tok)
                            if current_move:
                                print(current_move)
                            else:
                                break

                    winner = board.calc_winner()
                    if winner:
                        print(f'{winner} wins!')
                        print(board)

                    if board.is_full():
                        print('Cannot make any more moves. The board is full.')
                        print(board)

                    if board.is_game_over():
                        print('Game over.')
                        break

            else:
                print(f'Invalid input. {player1_name}, please, choose X or O.')

            if player1_tok in ['X', 'O']:
                break

        play_again = input('Play again? ').strip().lower()
        if play_again.startswith('n'):
            break
