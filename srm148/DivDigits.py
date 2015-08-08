"""
http://community.topcoder.com/stat?c=problem_statement&pm=1741

Single Round Match 148 Round 1 - Division II, Level One
Single Round Match 215 Round 1 - Division II, Level One
"""


class DivisorDigits:
    def howMany(self, number):
        digits = [0] * 11
        n = number
        while n:
            digits[n % 10] += 1
            n /= 10
        result = 0
        for digit, count in enumerate(digits):
            if digit > 0 and number % digit == 0:
                result += count
        return result
