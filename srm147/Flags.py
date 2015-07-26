"""
http://community.topcoder.com/stat?c=problem_statement&pm=4540

Single Round Match 147 Round 1 - Division I, Level Three
"""


class Flags:
    def numStripes(self, numFlags, forbidden):
        numFlags = int(numFlags)
        numColors = len(forbidden)
        check = [[True] * numColors for _ in range(numColors)]
        factors = [numColors] * numColors
        for i in range(numColors):
            row = forbidden[i].split(' ')
            for j in row:
                check[i][int(j)] = False
                factors[i] -= 1

        if max(factors) == 1:
            return (numFlags - numColors - 1) / sum(factors) + 2

        stripes = 1
        patterns = [[1] * numColors, [1] * numColors]
        totalPatterns = numColors
        current, next = 0, 1
        while totalPatterns < numFlags:
            stripes += 1
            for i in range(numColors):
                patterns[next][i] = sum([
                    patterns[current][j] if check[i][j] else 0
                    for j in range(numColors)
                ])
            current, next = next, current
            totalPatterns += sum(patterns[current])
        return stripes
