import random


class Player:
    def __init__(self, letter):
        self.letter = letter
    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        #return chossen squre for nxt move
        return random.choice(game.available_moves())
    


    

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        while True:
            square = input(self.letter + "'s turn, Input move(0-8): ")

            try:
                square = int(square)
                if square not in game.available_moves():
                    raise ValueError
                return square
            except:
                print("Invalid move, Try again ")
    
