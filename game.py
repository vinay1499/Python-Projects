import math
from player import HumanPlayer, RandomComputerPlayer



class TicTacToe:
    def __init__(self):
        self.board = [' 'for i in range(9)] # here we use a list to represent 3X3 board.
        self.current_winner = None # keeps track of current winner

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
        #just getting the rows
            print("| " + " | ".join(row) + '|')

    @staticmethod
    def print_board_nums():
        #0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3) ]

        for row in number_board:
            print("| " + " | ".join(row) + '|')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ' ]

    def empty_squares(self):
        return ' ' in self.board
    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # if valid move, then make the move (assing square to letter ) 
        #then return true. if invalid return false.
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    def winner(self, square, letter):
        # winner if 3 in a row anywhere.... we have to check the possibilities
        # first let's check the row
        row_ind = square //3
        row = self.board[row_ind*3 : (row_ind + 1)*3]
        if all([spot == letter for spot in row]):
            return True
        #check the columns
        col_ind = square %3
        column = [self.board[col_ind + i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        #check diagonals
        # but only if the square is an even number(0,2,4,6,8)
        # these are only moves possible to win a diagonal 

        if square %2 ==0:
            diagonal1 = [self.board[i] for i in [0,4,8]] #left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]] #right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True
        #if all of these checks fails we return false

        return False








def play(game, x_Player, o_Player, print_game = True):
    if print_game:
        game.print_board_nums()

    letter = 'X' #starting letter

    #iterate while the game still has empty square
    # we don't have to worry about the winner because we will just return that 
    # which breaks the loop]\

    while game.empty_squares():
        # get the move from appropriate player
        if letter =="O" :
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        #let's define a function to make a move
        if game.make_move(square,letter):
            if print_game:
                print(letter + f' makes a move to sqaure {square}')
                game.print_board()
                print(' ') #prints an empty line

            if game.current_winner:
                if print_game:
                    print(letter + ' Wins!')
                return letter


            letter = 'O' if letter == 'X' else 'X'

            if print_game:
                print("It\'s a tie")



if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)

