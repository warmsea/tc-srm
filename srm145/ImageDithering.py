"""
http://community.topcoder.com/stat?c=problem_statement&pm=1728

Single Round Match 145 Round 1 - Division II, Level One
Single Round Match 208 Round 1 - Division II, Level One
"""
import string


# In SRM 208, the class name is DitherCounter
class ImageDithering:
    def count(self, dithered, screen):
        checker = {}
        res = 0
        for color in string.uppercase:
            checker[color] = False
        for color in dithered:
            checker[color] = True
        for rows in screen:
            for color in rows:
                if checker[color]:
                    res += 1
        return res
