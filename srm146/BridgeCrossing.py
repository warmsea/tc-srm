"""
http://community.topcoder.com/stat?c=problem_statement&pm=1599

Single Round Match 146 Round 1 - Division II, Level Three
"""


class BridgeCrossing:
    def minTime(self, times):
        if len(times) == 1:
            return times[0]

        times = sorted(times)
        min_time = times[1]
        slowest_waiter = len(times) - 1

        while slowest_waiter >= 2:
            if slowest_waiter == 2:  # 3 people left
                min_time += times[0] + times[2]
                slowest_waiter -= 1
            else:  # more than 3 people left
                min_time += min([
                    times[0] + times[slowest_waiter] + times[1] * 2,
                    times[slowest_waiter] + times[slowest_waiter - 1] + times[0] * 2])
                slowest_waiter -= 2

        return min_time
