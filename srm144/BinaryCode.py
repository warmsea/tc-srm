"""SRM 144 Div 1 Problem 1, Div 2 Problem 2
Problem Statement: http://community.topcoder.com/stat?c=problem_statement&pm=1704
"""


class BinaryCode():
    def decode(self, message):
        message = map(int, message)
        size = len(message)
        r = [(size + 2) * [0], (size + 2) * [0]]
        for k in (0, 1):
            r[k][1] = k
            for i in range(2, size + 2):
                r[k][i] = message[i - 2] - r[k][i - 1] - r[k][i - 2]
                if r[k][i] != 0 and r[k][i] != 1:
                    r[k] = None
                    break
            if r[k] and r[k][-1] != 0:
                r[k] = None
            r[k] = ''.join(map(str, r[k][1:-1])) if r[k] else 'NONE'
        return tuple(r)
