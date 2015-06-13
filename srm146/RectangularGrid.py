"""
http://community.topcoder.com/stat?c=problem_statement&pm=1589

Single Round Match 146 Round 1 - Division I, Level One
Single Round Match 146 Round 1 - Division II, Level Two
"""


def combination(n, m):
    m = min(m, n - m)
    res = 1
    for i in range(m):
        res = res * (n - i) / (i + 1)
    return res


class RectangularGrid:
    def countRectangles(self, width, height):
        if width < height:
            width, height = height, width
        num = combination(width + 1, 2) * combination(height + 1, 2)
        for k in range(1, height + 1):
            num -= (width + 1 - k) * (height + 1 - k)
        return num
