"""
http://community.topcoder.com/stat?c=problem_statement&pm=1667

Single Round Match 147 Round 1 - Division II, Level One
"""


class CCipher:
    def decode(self, cipherText, shift):
        a = ord('A')
        decoder = [a + (c - shift if c >= shift else c - shift + 26) for c in range(26)]
        plain = [chr(decoder[ord(c) - a]) for c in cipherText]
        return ''.join(plain)
