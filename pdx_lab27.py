# Lab 27: Connect Four
from collections import namedtuple

Player = namedtuple('Player', ['name', 'color'])

class Game:
    def __init__(self):
        self.board = [['-' for x in range(7)] for y in range(6)]

    def __repr__(self):
        board = ''
        for row in self.board:
            board += '|'.join(row)
            board += '\n'
        return board

    def __get_height(self, position):
        counter = 0
        for i in range(len(self.board) - 1, -1, -1):
            find_token = self.board[i][position - 1]
            if find_token == '-':
                break
            counter += 1
        return counter

    def move(self, player, position):
        x = position - 1
        y = 5 - self.__get_height(position)
        if y < 0:
            raise IndexError('Error: Column full. Choose another.')
        self.board[y][x] = player.color

    def calc_winner(self):
        for y in range(len(self.board)-3):
            for x in range(len(self.board[y])-3):
                # horizontal match
                for i in range(4):
                    if self.board[y+i][x] == self.board[y+i][x+1] == self.board[y+i][x+2] == self.board[y+i][x+3] and self.board[y+i][x] != '-':
                        return self.board[y+i][x]
                # vertical match
                if self.board[y][x] == self.board[y+1][x] == self.board[y+2][x] == self.board[y+3][x] and self.board[y][x] != '-':
                    return self.board[y][x]
                # diagonal match
                if self.board[y+3][x] == self.board[y+2][x+1] == self.board[y+1][x+2] == self.board[y][x+3] and self.board[y][x+3] != '-':
                    return self.board[y][x+3]

                if self.board[y][x] == self.board[y+1][x+1] == self.board[y+2][y+2] == self.board[y+3][x+3] and self.board[y][x] != '-':
                    return self.board[x][y]

    def is_full(self):
        for row in self.board:
            for cell in row:
                if cell == '-':
                    return False
        return True

    def is_game_over(self):
        return self.calc_winner() or self.is_full()


if __name__ == '__main__':
    with open('connect-four-moves.txt') as moves_file:
        moves_list = []
        for line in moves_file:
            moves_list.append(int(line))

    game = Game()
    print("Let's play Connect Four!")
    player1 = Player('Player 1', 'Y')
    print(f'{player1.name}, your token is yellow.')
    player2 = Player('Player 2', 'R')
    print(f'{player2.name}, your token is red.')

    for i in range(len(moves_list)):
        print(game)
        if i % 2 == 0:
            current_player = player1
        else:
            current_player = player2

        while True:
            move = moves_list[i]
            try:
                position = move
                if position < 1 or position > 7:
                    raise ValueError
                game.move(current_player, position)
                break
            except ValueError:
                print('Error: Enter a number between 1 and 7.')
            except IndexError as e:
                print(e)

    print(game)
    # calculate winner
    winner = game.calc_winner()
    if winner:
        print(f'{winner} wins!')
    else:
        print('Board is full...')
