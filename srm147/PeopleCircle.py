"""
http://community.topcoder.com/stat?c=problem_statement&pm=1225

Single Round Match 147 Round 1 - Division I, Level One
Single Round Match 147 Round 1 - Division II, Level Two
"""


class PeopleCircle:
    def order(self, numMales, numFemales, K):
        numTotal = numMales + numFemales
        circle = ['M'] * numTotal
        numLeft = numTotal
        p = -1
        for _ in range(numFemales):
            offset = K % numLeft
            if offset == 0:  # One person can not be removed twice
                offset += numLeft
            while offset:
                p += 1
                if p >= numTotal:
                    p -= numTotal
                if circle[p] == 'M':
                    offset -= 1
            circle[p] = 'F'
            numLeft -= 1
        return ''.join(circle)
