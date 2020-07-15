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
