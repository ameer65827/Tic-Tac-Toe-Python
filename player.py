import random

# super class
from random import Random


class Player:
    def __init__(self, letter):
        self.letter = letter

    # we want all player to get next move when given a game
    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square



class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        square = None

        while True:
            # getting input from user for next move
            square = input(self.letter + "'s turn. Input move(0-8): ")

            #checking if input is valid
            try:
                square = int(square)  # raise ValueError if square is not int
                if square not in game.available_moves():
                    raise ValueError
                return square         # if all condition are satisfied(no error), that square is returned
            except:
                print("Invalid move, Try again !!!")





