"""SRM 144 Div 1 Problem 2
Problem statement: http://community.topcoder.com/stat?c=problem_statement&pm=1659
"""
from operator import mul


def permutation(n, m):
    return reduce(mul, range(n, n - m, -1))


def combination(n, m):
    m = min(m, n - m)
    res = 1
    for i in range(m):
        res = res * (n - i) / (i + 1)
    return res


class Lottery:
    def sortByOdds(self, rules):
        odds = []
        for rule in rules:
            name, rule = rule.split(': ')
            choices, blanks, fs, fu = rule.split(' ')
            choices = int(choices)
            blanks = int(blanks)
            fs = True if fs == 'T' else False
            fu = True if fu == 'T' else False
            odds.append((name, self.num_valid(choices, blanks, fs, fu)))
        odds = sorted(odds, lambda x, y: cmp(x[1], y[1]) or cmp(x[0], y[0]))
        print odds
        return [i[0] for i in odds]

    def num_valid(self, choices, blanks, fs, fu):
        if fu and fs:
            return combination(choices, blanks)
        elif fu and not fs:
            return permutation(choices, blanks)
        elif not fu and fs:
            return combination(choices + blanks - 1, blanks)
        else:
            return choices ** blanks
