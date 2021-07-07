class SnakesLadders:

    def __init__(self):
        self.complete = False
        self.p1 = 0
        self.p2 = 0
        self.turn = 1
        self.ladders_snakes = {2: 38, 7: 14, 8: 31, 15: 26, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 78: 98, 87: 94,
                               99: 80, 95: 75, 92: 88, 89: 68, 74: 53, 64: 60, 62: 19, 49: 11, 46: 25, 16: 6}

    def play(self, die1, die2):
        if self.complete:
            return 'Game over!'
        if die1 == die2:
            double = True
        else:
            double = False
        combodie = die1 + die2

        # Player 1
        if self.turn == 1:
            if self.p1 + combodie > 100:
                self.p1 = 100 - (combodie - (100 - self.p1))
            else:
                self.p1 += combodie
            if self.ladders_snakes.get(self.p1) is not None:
                self.p1 = self.ladders_snakes.get(self.p1)
            if not double:
                self.turn = 2
            if self.p1 == 100:
                self.complete = True
                return 'Player 1 Wins!'
            else:
                return f'Player 1 is on square {self.p1}'

        # Player 2
        if self.turn == 2:
            if self.p2 + combodie > 100:
                self.p2 = 100 - (combodie - (100 - self.p2))
            else:
                self.p2 += combodie
            if self.ladders_snakes.get(self.p2) is not None:
                self.p2 = self.ladders_snakes.get(self.p2)
            if not double:
                self.turn = 1
            if self.p2 == 100:
                self.complete = True
                return 'Player 2 Wins!'
            else:
                return f'Player 2 is on square {self.p2}'
