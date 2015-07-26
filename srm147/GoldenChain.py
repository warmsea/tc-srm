"""
http://community.topcoder.com/stat?c=problem_statement&pm=1355

Single Round Match 147 Round 1 - Division II, Level Three
"""


def knapsack_0_1(weights, prices, weight_limit):
    num_items = len(weights)
    max_price = [0] * (weight_limit + 1)
    for i in range(num_items):
        for w in range(weight_limit, 0, -1):
            put_out = max_price[w]
            if weights[i] <= w:
                put_in = prices[i] + max_price[w - weights[i]]
            else:
                put_in = 0
            max_price[w] = max([put_out, put_in])
    return max_price


class GoldenChain:
    def minCuts(self, sections):
        n = len(sections)
        a = knapsack_0_1(sections, [1] * n, n)
        for i in range(len(a)):
            if i + a[i] >= n:
                return i
        # Should never be here
        return n
