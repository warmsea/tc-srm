# Stable
# O(n) extra space for arrays
# O(n*lg(n)) time
# Do not require random access to data


def merge_sort(arr, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1

    if low >= high:
        return

    m = (low + high) / 2
    merge_sort(arr, low, m)
    merge_sort(arr, m + 1, high)

    work = [None] * (high - low + 1)
    i, j, k = low, m + 1, 0
    while i <= m and j <= high:
        if arr[i] < arr[j]:
            work[k] = arr[i]
            k += 1
            i += 1
        else:
            work[k] = arr[j]
            k += 1
            j += 1
    while i <= m:
        work[k] = arr[i]
        k += 1
        i += 1
    while j <= high:
        work[k] = arr[j]
        k += 1
        j += 1
    arr[low:high + 1] = work[:]


if __name__ == '__main__':
    data = [1, 6, 5, 8, 4, 7, 3, 9, 2]
    merge_sort(data)
    print data
