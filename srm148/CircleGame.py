"""
http://community.topcoder.com/stat?c=problem_statement&pm=1735

Single Round Match 148 Round 1 - Division I, Level One
"""


class CircleGame:
    def cardsLeft(self, deck):
        characters = [c for c in '0A23456789TJQK']
        values = {}
        for i, j in enumerate(characters):
            values[j] = i
        cards = [values[c] for c in deck]
        while True:
            finished = True
            i = 0
            while i < len(cards):
                if cards[i] == 13:
                    cards[i:i + 1] = []
                    finished = False
                elif i == len(cards) - 1 and cards[i] + cards[0] == 13:
                    cards[i:] = []
                    cards[:1] = []
                    finished = False
                elif i < len(cards) - 1 and cards[i] + cards[i + 1] == 13:
                    cards[i:i + 2] = []
                    finished = False
                else:
                    i += 1
            if finished:
                break
        return len(cards)
