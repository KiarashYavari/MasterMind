import random
from consts import *


class Game(object):
    def __init__(self, length=GAME_LENGTH):
        self.length = length
        self.initial = []
        self.turns = 0
        self.is_won = False
        self.is_ended = False

    # process the initial state of colors
    def new_game(self):
        while len(self.initial) < self.length:
            random_number = random.randint(MIN_COLOR, MAX_COLOR)
            if random_number not in self.initial:
                self.initial.append(random_number)
        self.initial = [COLORS[i] for i in self.initial]  # turn the numbers of colors to the names of colors

    # start of guessing the colors
    def turn(self):
        if self.is_ended:
            return
        # print(guess)
        # for turn in range(self.length):  # took colors and split them with-->,
        guess = input()
        guess = guess.split(",")
        white = 0
        black = 0
        for items in range(self.length):  # check the black and white point of player input colors
            if guess[items] == self.initial[items]:
                black += 1
            elif guess[items] in self.initial:
                white += 1
        self.turns += 1
        print("black: {}  white: {}".format(black, white))
        self.check_state(black)

    # definition of to_string() --> split the initial_colors for printing
    def to_string(self):
        return ",".join(self.initial)

    # check the if the user guess the right state
    def check_state(self, black):
        if self.check_win(black):
            print("you won =))")
            self.end()
        elif self.check_lost():
            print("you lose =(( the colors were {}".format(self.to_string()))
            self.end()

    # losing condition
    def check_lost(self):
        return (self.turns == MAX_TURNS) and not self.is_won

    # wining condition
    def check_win(self, black):
        return self.length == black

    # check if the game come to end or not
    def end(self):
        self.is_ended = True


game = Game()
game.new_game()
for index in range(MAX_TURNS):
    game.turn()
