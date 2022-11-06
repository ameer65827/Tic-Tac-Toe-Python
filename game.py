
from player import HumanPlayer, RandomComputerPlayer
from time import sleep

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]     # single list to represent 3x3 board
        self.current_winner = None

    # printing board with letters
    def print_board(self):
        # one row at a time
        for row in [self.board[i*3: (i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    @staticmethod
    def print_board_nums():
        # prints | 0 | 1 | 2 | etc 
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    
    def available_moves(self):
        # finding all available free square (that is -> ' ')
        return [i for i, spot in enumerate(self.board) if spot == ' ']


    # checking if empty square available
    def empty_squares(self):
        return ' ' in self.board

    

    # make move fn
    def make_move(self, square, letter):
        # better if we check the square is free
        self.board[square] = letter
        
        # after move checking if won
        if self.victory(square, letter):
            self.current_winner = letter
        return
    
    def victory(self, square, letter):

        # checking row
        row_indx = square // 3
        row = self.board[row_indx*3: (row_indx + 1)*3]
        if all(spot == letter for spot in row):
            return True
        
        # checking row
        col_indx = square % 3
        col = [self.board[col_indx + (i*3)] for i in range(3)]
        if all(spot == letter for spot in col):
            return True
        
        #checking diagonals
        # we know if the move is not even, then it cannot form a diagonal, so first check even
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all(spot == letter for spot in diagonal1):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all(spot == letter for spot in diagonal2):
                return True
        # if all of these fails
        return False
        



# play function
def play(game, x_player, o_player):
    # RETURN THE WINNER
    
    # print num_board
    game.print_board_nums()

    letter = 'X'

    while game.empty_squares():

        if letter == 'X':
            square = x_player.get_move(game)
            sleep(0.2)
        else:
            square = o_player.get_move(game)
            sleep(1)
        
        # now we know next move, --> make the move
        game.make_move(square, letter)
        print(letter + f" makes a move to square {square}")
        game.print_board()
        print()

        if game.current_winner:
            print(letter + " WINS $$$")
            return letter

        # swap letter, next player
        letter = 'O' if letter == 'X' else 'X'
        
    # after while loop ends
    print("It's a Tie ")



if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    my_game = TicTacToe()

    play(my_game, x_player, o_player)

        

    
