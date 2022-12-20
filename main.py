from time import sleep
from players import *
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.winning_set = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
        self.winner = None

    @staticmethod
    def print_board(board):
        print('\t      |      |      ')
        print('\t   {}  |  {}   |  {}'.format(board[0], board[1], board[2]))
        print('\t------|------|------')

        print('\t   {}  |  {}   |  {}'.format(board[3], board[4], board[5]))
        print('\t------|------|------')

        print('\t   {}  |  {}   |  {}'.format(board[6], board[7], board[8]))
        print('\t      |      |      ')
        
    def available_moves(self):
        return [indx for indx, spot in enumerate(self.board) if spot == ' ']

    def make_move(self, square, letter):
        self.board[square] = letter

    def check_winner(self,board , letter):
        # if self.winning_set combination contain consecutive letters -> letter won
        for rcd in self.winning_set:
            if all(board[spot] == letter for spot in rcd):
                return True
        return False


# global function
def play(x_player, o_player, game):
    
    # printing numbered board for reference
    print('\nNumbered Board')
    TicTacToe.print_board([_ for _ in range(1, 10)])

    sleep(0.5)

    letter = 'X'  # let first player be 'X'

    # loop untile no further moves
    while game.available_moves():
        if letter == 'X':
            move = x_player.get_move(game, letter)
        else:
            move = o_player.get_move(game)
        
        game.make_move(move, letter)

        # print changes
        print()
        print('{}_PLAYER'.format(letter))
        sleep(0.5)
        TicTacToe.print_board(game.board)
        print()
        sleep(0.5)

        # check winner
        if game.check_winner(game.board, letter):
            print("{} WON $$$".format(letter) )
            return 1
        
        # swap the letter
        letter = 'O' if letter == 'X' else 'X'

    print("IT'S A TIE")
    return 0                

if __name__ == '__main__':
    X_player = ComputerPlayer('X')
    O_player = HumanPlayer('O')

    game = TicTacToe()

    # STARTING GAME
    play(X_player, O_player, game)
    
    
    

