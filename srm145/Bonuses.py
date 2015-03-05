"""
http://community.topcoder.com/stat?c=problem_statement&pm=1777

Single Round Match 156 Round 1 - Division II, Level One
"""


class Bonuses:
    def getDivision(self, points):
        total = sum(points)
        people = [{'position': i, 'points': p, 'bonus': 100 * p / total}
                  for i, p in enumerate(points)]
        people = sorted(people, lambda x, y: -cmp(x['points'], y['points']) or
                                             cmp(x['position'], y['position']))
        left = 100 - sum([p['bonus'] for p in people])
        for i in range(len(people)):
            if left:
                people[i]['bonus'] += 1
                left -= 1
            else:
                break
        people = sorted(people, lambda x, y: cmp(x['position'], y['position']))
        return [p['bonus'] for p in people]
