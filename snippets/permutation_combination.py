from operator import mul


def permutation(n, r):
    return reduce(mul, range(n, n - r, -1))


def combination(n, r):
    r = min(r, n - r)
    res = 1
    for i in range(r):
        res = res * (n - i) / (i + 1)
    return res


def full_permutations(pool, pos=0):
    if pos == len(pool):
        print pool
    for i in range(pos, len(pool)):
        pool[i], pool[pos] = pool[pos], pool[i]
        full_permutations(pool, pos + 1)
        pool[i], pool[pos] = pool[pos], pool[i]


def combinations(n, r, selected=[]):
    if r == 0:
        print selected
    if n <= 0 or r <= 0 or n < r:
        return
    combinations(n - 1, r, selected)
    selected.append(n)
    combinations(n - 1, r - 1, selected)
    selected.pop()


combinations(5, 3)


def full_permutations_2(n):
    if n <= 1:
        return
    pool = range(n)
    while True:
        print pool
        swap = -1
        for i in range(n - 2, -1, -1):
            if pool[i] < pool[i + 1]:
                swap = i
                break
        if swap < 0:
            break
        i_min = -1
        for i in range(swap + 1, n):
            if pool[swap] > pool[i]:
                continue
            elif i_min == -1 or pool[i] < pool[i_min]:
                i_min = i
        if i_min == swap:
            break
        pool[swap], pool[i_min] = pool[i_min], pool[swap]
        pool[swap + 1:] = sorted(pool[swap + 1:])


class Permutations():
    def __init__(self, pool, r):
        self.pool = pool
        self.r = r
        n = len(pool)
        n_minus_r = n - r
        if n_minus_r < 0:
            self.stopped = True
        else:
            self.stopped = False
            self.indices = range(n)
            self.cycles = range(n, n_minus_r, -1)

    def __iter__(self):
        return self

    def next(self):
        if self.stopped:
            raise StopIteration
        r = self.r
        indices = self.indices
        result = tuple([self.pool[indices[i]] for i in range(r)])
        cycles = self.cycles
        i = r - 1
        while i >= 0:
            j = cycles[i] - 1
            if j > 0:
                cycles[i] = j
                indices[i], indices[-j] = indices[-j], indices[i]
                return result
            cycles[i] = len(indices) - i
            n1 = len(indices) - 1
            assert n1 >= 0
            num = indices[i]
            for k in range(i, n1):
                indices[k] = indices[k + 1]
            indices[n1] = num
            i -= 1
        self.stopped = True
        return result


class Combinations():
    def __init__(self, pool, indices, r):
        self.pool_w = pool
        self.indices = indices
        self.r = r
        self.last_result = None
        self.stopped = r > len(pool)

    def get_maximum(self, i):
        return i + len(self.pool_w) - self.r

    def max_index(self, j):
        return self.indices[j - 1] + 1

    def __iter__(self):
        return self

    def next(self):
        if self.stopped:
            raise StopIteration
        if self.last_result is None:
            # On the first pass, initialize result tuple using the indices
            result = [None] * self.r
            for i in xrange(self.r):
                index = self.indices[i]
                result[i] = self.pool_w[index]
        else:
            # Copy the previous result
            result = self.last_result[:]
            # Scan indices right-to-left until finding one that is not at its
            # maximum
            i = self.r - 1
            while i >= 0 and self.indices[i] == self.get_maximum(i):
                i -= 1

            # If i is negative, then the indices are all at their maximum value
            # and we're done
            if i < 0:
                self.stopped = True
                raise StopIteration

            # Increment the current index which we know is not at its maximum.
            # Then move back to the right setting each index to its lowest
            # possible value
            self.indices[i] += 1
            for j in xrange(i + 1, self.r):
                self.indices[j] = self.max_index(j)

            # Update the result for the new indices starting with i, the
            # leftmost index that changed
            for i in xrange(i, self.r):
                index = self.indices[i]
                w_elem = self.pool_w[index]
                result[i] = w_elem
        self.last_result = result
        return tuple(result)
