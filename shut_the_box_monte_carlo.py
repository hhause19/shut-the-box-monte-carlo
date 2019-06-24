#!/usr/bin/env python3

import random
from itertools import combinations

STRATEGY = 'shortest'

class Game:
    def __init__(self):
        self.box = list(range(1,10))
        self.won = False

    def play(self):
        while True:
            if not self.turn():
                break

    def turn(self):
        roll = self.roll()
        combos  = self.get_combinations()

        available_sets = []
        for combo in combos:
            if sum(combo) == roll:
                available_sets.append(combo)

        if available_sets:
            self.choose(roll, available_sets)
            return True
        else:
            return False

    def roll(self):
        return random.randint(2,12)

    def choose(self, roll, available_sets):
        if STRATEGY == 'first':
            chosen_set = available_sets[0]

        elif STRATEGY == 'random':
            i = random.randint(0, len(available_sets))
            chosen_set = available_sets[i - 1]

        elif STRATEGY == 'shortest':
            available_sets.sort(key=len)
            chosen_set = available_sets[0]

        self.box = [n for n in self.box if n not in chosen_set]

        if len(self.box) == 0:
            self.won = True

        return

    def get_combinations(self):
        all_combiations = []

        if len(self.box) == 1:
            return [(self.box[0],)]

        for i in range(len(self.box)):
            c = combinations(self.box, i)
            all_combiations.extend(list(c))

        return all_combiations

def play_game():
    game = Game()
    game.play()
    return game.won


def main():
    plays = 100000
    wins = 0
    for x in range(plays):
        if play_game():
            wins += 1

    print('Wins: ', wins)
    print('Games: ', plays)
    print('Win Percent: ', round((wins / plays * 100), 2), '%')

if __name__ == "__main__":
    main()
