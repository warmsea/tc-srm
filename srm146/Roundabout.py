"""
http://community.topcoder.com/stat?c=problem_statement&pm=1605

Single Round Match 146 Round 1 - Division I, Level Three
"""


class Roundabout:
    # Total time
    time = 0
    # Clear up time
    clear_up_time = 0
    # 0 to 4
    four = [0, 1, 2, 3]
    # Order of directions
    directions = ['W', 'S', 'E', 'N']
    # The coming cars
    queues = None
    # Cars in the west/south/east/north of the roundabout.
    insides = ['-', '-', '-', '-']
    # Cars waiting in the west/south/east/north entry point.
    waitings = [[], [], [], []]

    def clearUpTime(self, north, east, south, west):
        self.queues = [west, south, east, north]
        min_time = max([len(q) for q in self.queues])

        while True:
            entered_cars = self.cars_enter()
            self.cars_leave(entered_cars)
            self.more_waiting_cars()
            if self.time > min_time:
                if all([i == '-' for i in self.insides]) and all([len(w) == 0 for w in self.waitings]):
                    break
            self.time += 1

        return self.clear_up_time

    def more_waiting_cars(self):
        for i in self.four:
            if self.time < len(self.queues[i]):
                next_car = self.queues[i][self.time]
                if next_car != '-':
                    self.waitings[i].append(next_car)

    def cars_enter(self):
        entered_cars = [None] * 4
        for i in self.four:
            if len(self.waitings[i]) > 0 and len(self.waitings[i - 1]) == 0 and self.insides[i - 1] == '-':
                entered_cars[i] = self.waitings[i][0]
        if not any(entered_cars) and all([len(w) > 0 for w in self.waitings]) and self.insides[2] == '-':
            entered_cars[3] = self.waitings[3][0]
        for i in self.four:
            if entered_cars[i]:
                self.waitings[i].pop(0)
        return entered_cars

    def cars_leave(self, entered_cars):
        for i in self.four:
            if self.insides[i] == self.directions[i]:
                self.insides[i] = '-'
                self.clear_up_time = self.time
        new_insides = ['-', '-', '-', '-']
        for i in self.four:
            new_insides[i] = entered_cars[i] or self.insides[i - 1]
        self.insides = new_insides
