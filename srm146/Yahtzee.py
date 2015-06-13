"""
http://community.topcoder.com/stat?c=problem_statement&pm=1692

Single Round Match 146 Round 1 - Division II, Level One
Single Round Match 212 Round 1 - Division II, Level One
"""


class Yahtzee:
    def maxPoints(self, toss):
        sums = [0] * 7
        for value in toss:
            sums[value] += value
        return max(sums)
