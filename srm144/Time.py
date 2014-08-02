"""SRM 144 Div 2 Problem 1
Problem Statement: http://community.topcoder.com/stat?c=problem_statement&pm=1708
"""


class Time:
    def whatTime(self, seconds):
        return ':'.join(map(str, [int(seconds / 3600), int(seconds % 3600 / 60), seconds % 60]))
