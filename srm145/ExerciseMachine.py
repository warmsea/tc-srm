"""
http://community.topcoder.com/stat?c=problem_statement&pm=1675

Single Round Match 145 Round 1 - Division II, Level Two
"""


class ExerciseMachine:
    def getPercentages(self, times):
        h, m, s = map(int, times.split(':'))
        seconds = h * 3600 + m * 60 + s
        for i in [100, 50, 25, 20, 10, 5, 4, 2, 1]:
            if seconds % i == 0:
                return i - 1
