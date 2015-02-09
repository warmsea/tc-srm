"""
http://community.topcoder.com/stat?c=problem_statement&pm=1697

Single Round Match 144 Round 1 - Division II, Level Three
"""
from operator import add


class PowerOutage:
    nodes = {}

    def estimateTimeOut(self, fromJunction, toJunction, ductLength):
        for i in range(len(fromJunction)):
            if fromJunction[i] not in self.nodes:
                self.nodes[fromJunction[i]] = []
            self.nodes[fromJunction[i]].append((toJunction[i], ductLength[i]))
            if toJunction[i] not in self.nodes:
                self.nodes[toJunction[i]] = []
            self.nodes[toJunction[i]].append((fromJunction[i], ductLength[i]))
        longest_path = self.longest_path(0)
        print self.nodes
        return reduce(add, ductLength) * 2 - longest_path

    def longest_path(self, start, last=-1):
        longest_path = 0
        if start in self.nodes:
            for i, distance in self.nodes[start]:
                if i == last:
                    continue
                cur_longest = distance + self.longest_path(i, start)
                if cur_longest > longest_path:
                    longest_path = cur_longest
        return longest_path
