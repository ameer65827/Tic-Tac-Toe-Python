from player import HumanPlayer, RandomComputerPlayer
from time import sleep



class TicTacToe:

    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.winner = None
    
    #print numbered board
    @staticmethod
    def print_board(board):
        
        print("\n")  
        print("\t     |     |")  
        print("\t  {}  |  {}  |  {}".format(board[0], board[1], board[2]))  
        print('\t_____|_____|_____')  
    
        print("\t     |     |")  
        print("\t  {}  |  {}  |  {}".format(board[3], board[4], board[5]))  
        print('\t_____|_____|_____')  
    
        print("\t     |     |")  
    
        print("\t  {}  |  {}  |  {}".format(board[6], board[7], board[8]))  
        print("\t     |     |")  
        print("\n")  
                
    # def print_board(self):
    #     for row in [self.board[i*3: (i+1)*3] for i in range(3)]:
    #         print('| ' + ' | '.join(row) + ' |')
    
    def available_moves(self):
        return [ind for ind, spot in enumerate(self.board) if spot == ' ']
    
    def make_move(self, square, letter):
        self.board[square] = letter

    def victory(self, square, letter):

        # row
        row_indx = square // 3
        row = self.board[row_indx*3: (row_indx + 1)*3]
        if row.count(letter) == 3:
            return True
        
        # column
        col_indx = square % 3
        col = [self.board[col_indx + (i*3) ] for i in range(3)]
        if all(spot == letter for spot in col):
            return True
        
        # diagonals
        if square%2:
            if all(self.board[i] == letter for i in [0, 4, 8]):
                return True
            if all(self.board[i] == letter for i in [2, 4, 6]):
                return True
        return False
            
    
def play(x_player, o_player, game):
    game.print_board([val for val in range(1, 9+1)])
    
    letter = 'X'  # let X is the first player
    
    while game.available_moves():
        if letter == 'X':
            square = x_player.get_move(game)
        else:
            square = o_player.get_move(game)

        # make the move
        game.make_move(square, letter)
        sleep(0.5)
        print(letter + f" makes a move to square {square}")
        game.print_board(game.board)
        print()

        #check victory
        if game.victory(square, letter):
            game.winner = letter
            print(letter + " WON $$$")
            return letter
        # swap letter, next player
        letter = 'X' if letter == 'O' else 'O'

    print("it's a TIE")



if __name__ == '__main__':
    print("Type 'BOT' for computer oponent")
    print()
    player1 = input("Enter player 'X' name:- ")
    player2 = input("Enter player 'O' name:- ")
    print()

    x_player = None
    o_player = None

    if player1 == 'BOT':
        x_player = RandomComputerPlayer("{} (X)".format("BOT"))
    else:
        x_player = HumanPlayer("{} (X)".format(player1))

    if player2 == 'BOT':
        o_player = RandomComputerPlayer("{} (O)".format("BOT"))
    else:
        o_player = HumanPlayer("{} (O)".format(player1))


    game = TicTacToe()
    play(x_player, o_player, game)