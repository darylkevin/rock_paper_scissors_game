"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""


import random
import time

# List of valid moves for the game. This can be modified to your liking.
# e.g. You can modify it to the rules of rock-paper-scissors-lizard-spock.
moves = ['rock','paper','scissors']

"""The Player class is the parent class for all of the Players in
this game"""

# This player class will always return 'rock'
class Player:
    def move(self):
        return moves[0]

    def learn(self, my_move, their_move):
        pass

# This player class will return a random move each time according to the
# moves in the moves list.

class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

# This player class can be used by a human player

class HumanPlayer(Player):
    def move(self):
        # A lower function is called to accomodate both capital and lower
        # case input from the player
        move = input ('Rock, Paper, Scissors?\n'
                      'or "q" to quit. >>>').lower()

        # This checks if your input is included in the list of valid moves
        if move in moves:
            return move
        elif move == 'q':
            exit()
        else:
            return self.move()

# This player class that returns the move previously played by the opponent
class ReflectPlayer(Player):
    # This handles the intial state wher there are no moves played yet.
    def __init__(self):
        super().__init__()
        self.their_move = None

    def learn(self, my_move, thier_move):
        self.their_move = their_move
        return self.their_move

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        return self.their_move

# This player class cycles through all the possible moves in the list of moves
class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.counter = 0

# This implements the cycling nature of the moves. The code is simplified to
# handle future addition of moves in the moves list.
    def move(self):
        # Replace '3' with number of items in moves in case more moves are 
        # added to the list.
        remainder = self.counter % 3
        move = moves[remainder]
        self.counter += 1
        return move
