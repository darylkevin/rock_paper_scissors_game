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

# This function states the rules for winning a round. Additional conditions can
# be inserted depending on the rules of the game.
def beats(self, one, two):
    if ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock')):
        print('*** PLAYER ONE WINS ***')
        return 1
    elif ((two == 'rock' and one == 'scissors') or
            (two == 'scissors' and one == 'paper') or
            (two == 'paper' and one == 'rock')):
        print('*** PLAYER TWO WINS ***')
        return 2
    elif one == two:
        print('*** TIE ***')

# This sets the condition for winning the game.
def winner(self, score1, score2):
    if score1 > score2:
        print('*** PLAYER ONE WINS THE GAME!!! ***')
    elif score1 < score2:
        print('*** PLAYER TWO WINS THE GAME!!! ***')
    elif score1 == score2:
        print('*** THE GAME IS A TIE!!! ***')

# Randomizes the player matchups
def opponent():
    opponents = [Player(), RandomPlayer(), ReflectPlayer(),
            CyclePlayer(), HumanPlayer()]
    return random.choice(opponents)

# Option to play the game again
def play_again():
    answer = input('Do you want to play again?\n'
            '(Y)es or (N)o? >>>').lower()
    if answer == 'y':
        game = Game(opponent(), opponent())
        game.play_game()
    elif answer = 'n':
        exit()
    else:
        play_again()
