"""
http://community.topcoder.com/stat?c=problem_statement&pm=1708

Single Round Match 144 Round 1 - Division II, Level One
"""


class Time:
    def whatTime(self, seconds):
        return ':'.join(map(str, [int(seconds / 3600), int(seconds % 3600 / 60), seconds % 60]))
