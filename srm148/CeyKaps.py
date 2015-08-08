"""
http://community.topcoder.com/stat?c=problem_statement&pm=1740

Single Round Match 148 Round 1 - Division II, Level Two
"""

class CeyKaps:
    def decipher(self, typed, switches):
        for item in switches:
            left, right = item[0], item[2]
            typed = typed.replace(left, '_')
            typed = typed.replace(right, left)
            typed = typed.replace('_', right)
        return typed
