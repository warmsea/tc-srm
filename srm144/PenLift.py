"""
http://community.topcoder.com/stat?c=problem_statement&pm=1649

Single Round Match 144 Round 1 - Division I, Level Three
"""


class PenLift:
    def numTimes(self, segments, n):
        horizontals, verticals = self.merge_overlaps(segments)
        components = self.divide_to_components(horizontals, verticals)
        for c in components:
            print c
        lifts = -1
        for component in components:
            num_odds = self.count_odds(component)
            if n % 2:
                lifts += max(1, num_odds / 2)
            else:
                lifts += 1
        return lifts

    def merge_overlaps(self, segments):
        horizontals, verticals = {}, {}
        for segment in segments:
            x1, y1, x2, y2 = map(int, segment.split(' '))
            if y1 == y2:
                if y1 not in horizontals:
                    horizontals[y1] = []
                horizontals[y1].append([x1, x2] if x1 < x2 else [x2, x1])
            else:  # x1 == x2
                if x1 not in verticals:
                    verticals[x1] = []
                verticals[x1].append([y1, y2] if y1 < y2 else [y2, y1])
        for y in horizontals:
            horizontals[y] = self.get_merged_segments(horizontals[y])
        for x in verticals:
            verticals[x] = self.get_merged_segments(verticals[x])
        return horizontals, verticals

    def get_merged_segments(self, segments):
        segments = sorted(segments, lambda a, b: cmp(a[0], b[0]))
        merged = []
        cur = segments[0]
        for seg in segments:
            if seg[0] <= cur[1]:
                cur[1] = max(cur[1], seg[1])
            else:
                merged.append(cur)
                cur = seg
        merged.append(cur)
        return merged

    def divide_to_components(self, horizontals, verticals):
        segments = []
        num_h, num_v = 0, 0
        for y in horizontals:
            for x1, x2 in horizontals[y]:
                segments.append((x1, y, x2, y))
                num_h += 1
        for x in verticals:
            for y1, y2 in verticals[x]:
                segments.append((x, y1, x, y2))
                num_v += 1
        total = num_h + num_v
        crossed = dict([(i, []) for i in range(total)])
        for i in range(num_h):
            for j in range(num_h, total):
                if self.is_crossed(segments[i], segments[j]):
                    crossed[i].append(j)
                    crossed[j].append(i)
        divided = [False] * total
        count_down = total
        components = []
        while count_down:
            cur = []
            i = divided.index(False)
            cur.append(i)
            to_cross = [i]
            divided[i] = True
            count_down -= 1
            while len(to_cross):
                i = to_cross.pop()
                for j in crossed[i]:
                    if not divided[j]:
                        cur.append(j)
                        to_cross.append(j)
                        divided[j] = True
                        count_down -= 1
            components.append([segments[k] for k in cur])
        return components

    def is_crossed(self, h, v):
        return v[1] <= h[1] <= v[3] and h[0] <= v[0] <= h[2]

    def count_odds(self, component):
        ends = {}
        for x1, y1, x2, y2 in component:
            self.add_point_to(ends, x1, y1)
            self.add_point_to(ends, x2, y2)
        num_odds = 0
        for point in ends:
            if ends[point] % 2 == 1:
                num_odds += 1
        return num_odds

    def add_point_to(self, ends, x, y):
        k = '%s,%s' % (x, y)
        if k not in ends:
            ends[k] = 1
        else:
            ends[k] += 1
