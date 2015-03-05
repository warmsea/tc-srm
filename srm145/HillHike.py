"""
http://community.topcoder.com/stat?c=problem_statement&pm=1158

Single Round Match 145 Round 1 - Division I, Level Three
"""


class HillHike:
    def numPaths(self, distance, maxHeight, landmarks):
        self.landmarks = landmarks
        numLandmarks = len(landmarks)
        table = [[[[0
                    for l in range(numLandmarks + 2)]  # landmarks index
                   for mh in range(2)]  # meet max height or not
                  for h in range(maxHeight + 1)]  # height
                 for d in range(distance + 1)]  # distance
        table[0][0][0][0] = 1

        for d in range(distance):
            for h in range(min([d, maxHeight, distance - d]) + 1):
                for mh in range(2):
                    for l in range(numLandmarks + 2):
                        lc = table[d][h][mh][l]  # local path count
                        if not lc:
                            continue
                        nl = self.hitLandmark(l, h)  # landmark index of the next meter
                        if h < maxHeight and (h > 0 or d == 0):  # rising
                            table[d + 1][h + 1][mh or (1 if h + 1 == maxHeight else 0)][nl] += lc
                        if h > 0:  # level and failing
                            table[d + 1][h][mh][nl] += lc
                            table[d + 1][h - 1][mh][nl] += lc
        return table[distance][0][1][numLandmarks]

    def hitLandmark(self, landmarkIndex, height):
        if landmarkIndex < len(self.landmarks) and self.landmarks[landmarkIndex] == height:
            return landmarkIndex + 1
        else:
            return landmarkIndex
