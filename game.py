


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
        # return [i for i, spot in enumerate(self.board) if sport == ' ']
        moves = []
        for i, spot in enumerate(self.board):
            if spot == ' ':
                moves.append(i)
        return moves
    
    # checking if empty square available
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count()
    

        

# play function
def play(game, x_player, o_player):
    
    # print num_board
    game.print_board_num()

    letter = 'X'

    while game.empty_squares():
        

        if letter == 'X':
            pass
    