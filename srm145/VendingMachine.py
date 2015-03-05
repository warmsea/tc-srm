"""
http://community.topcoder.com/stat?c=problem_statement&pm=1130

Single Round Match 145 Round 1 - Division I, Level Two
Single Round Match 145 Round 1 - Division II, Level Three
"""
import re


class VendingMachine:
    def motorUse(self, prices, purchases):
        self.prices = [map(int, row.split(' ')) for row in prices]
        self.numColumns = len(self.prices[0])
        self.priceSum = [0] * self.numColumns
        for col in range(self.numColumns):
            self.priceSum[col] = sum([self.prices[i][col] for i in range(len(prices))])
        self.total = 0
        self.current = 0
        lastT = -5
        purchaseSpliter = re.compile('[,:]')
        for purchase in purchases:
            i, j, t = map(int, purchaseSpliter.split(purchase))
            if t - lastT >= 5:
                high = self.findHigh()
                self.moveTo(high)
            self.moveTo(j)
            lastT = t
            if self.prices[i][j]:
                self.priceSum[j] -= self.prices[i][j]
                self.prices[i][j] = 0
            else:
                return -1
        self.moveTo(self.findHigh())
        return self.total

    def findHigh(self):
        high, highP = 0, 0
        for i, p in enumerate(self.priceSum):
            if p > highP:
                high, highP = i, p
        return high

    def moveTo(self, after):
        shifts = abs(after - self.current)
        shifts = min(shifts, self.numColumns - shifts)
        self.total += shifts
        self.current = after
