import random

class Player:
    def __init__(self, letter):
        self.letter = letter
    
    def get_move(self):
        pass

class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    # return the move made by Computer
    # def get_move(self, game):
        # return random.choice(game.available_moves())

    # just more intelligent moves
    def get_move(self, game):
        move = random.choice(game.available_moves())
        for rcd in game.winning_set:                # rcd -> row col diagonal.
            if any(game.board[spot] == self.letter for spot in rcd):
                count_empty = 0
                count_self = 0
                empty_spots = []
                for e in rcd:
                    if game.board[e] == ' ':
                        count_empty += 1                # counts no. of empty spot
                        empty_spots.append(e)
                    elif game.board[e] == self.letter:
                        count_self += 1
                if count_empty == 1 and count_self == 2:   # one move win
                    return empty_spots[0]
                elif count_empty == 2:
                    move = empty_spots[0]
        return move

    def one_move_win_check(self, game):
        move = -1
        for rcd in game.winning_set:                    # rcd -> row col diagonal.
            if any(game.board[spot] == self.letter for spot in rcd):
                count_empty = 0
                count_self = 0                          # self -> current player letter
                empty_spots = []
                for e in rcd:
                    if game.board[e] == ' ':
                        count_empty += 1                # counts no. of empty spot
                        empty_spots.append(e)
                    elif game.board[e] == self.letter:
                        count_self += 1
                if count_self == 2 and count_empty == 1:
                    return empty_spots[0]
                    
        return move


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    # get move from user and return it
    def get_move(self, game):
        while True:
            inp = input("Your turn, Input move(1-9): ")

            try:
                inp = int(inp) - 1
                if inp in game.available_moves():
                    return inp
                else:
                    raise ValueError
            except:
                print("INVALID MOVE, TRY AGAIN !!!")
    def one_move_win_check(self, game):
        move = -1
        for rcd in game.winning_set:                    # rcd -> row col diagonal.
            if any(game.board[spot] == self.letter for spot in rcd):
                count_empty = 0
                count_self = 0                          # self -> current player letter
                empty_spots = []
                for e in rcd:
                    if game.board[e] == ' ':
                        count_empty += 1                # counts no. of empty spot
                        empty_spots.append(e)
                    elif game.board[e] == self.letter:
                        count_self += 1
                if count_self == 2 and count_empty == 1:
                     return empty_spots[0]
                    
        return move
