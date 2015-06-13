"""
http://community.topcoder.com/stat?c=problem_statement&pm=1541

Single Round Match 146 Round 1 - Division I, Level Two
"""


class Masterbrain:
    def possibleSecrets(self, guesses, results):
        possibles = 0
        for secret in self.secret_generator():
            lies = 0
            for i in range(len(guesses)):
                if self.get_result(secret, guesses[i]) != results[i]:
                    lies += 1
            if lies == 1:
                possibles += 1
        return possibles

    def secret_generator(self):
        for a in range(1, 8):
            for b in range(1, 8):
                for c in range(1, 8):
                    for d in range(1, 8):
                        yield ''.join(map(str, [a, b, c, d]))

    def get_result(self, secret, guess):
        secret = list(secret)
        guess = list(guess)
        b, w = 0, 0
        for i in range(4):
            if guess[i] == secret[i]:
                guess[i] = 'x'
                secret[i] = 'y'
                b += 1
        for i in range(4):
            for j in range(4):
                if guess[i] == secret[j]:
                    guess[i] = 'x'
                    secret[j] = 'y'
                    w += 1
        return '%db %dw' % (b, w)
