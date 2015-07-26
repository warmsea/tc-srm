"""
http://community.topcoder.com/stat?c=problem_statement&pm=1520

Single Round Match 147 Round 1 - Division I, Level Two
"""
from fractions import Fraction


class Dragons:
    def snaug(self, initialFood, rounds):
        current, next = 0, 1
        food = [[Fraction(f) for f in initialFood], [Fraction(f) for f in initialFood]]
        for _ in range(rounds):
            for i in range(6):
                food[next][i] = Fraction(0)
                for j in range(6):
                    if i / 2 != j / 2:
                        food[next][i] += food[current][j] / 4
            current, next = next, current
        return food[current][2]
