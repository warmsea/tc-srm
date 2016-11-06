# Stable
# O(n) extra space for arrays
# O(n*lg(n)) time
# Do not require random access to data


def merge_sort(arr):
    n = len(arr)
    width = 1
    while width < n:
        i = 0
        while i < n:
            merge(arr, i, i + 2 * width)
            i += 2 * width
        width *= 2


def merge(arr, low, high):
    m = low + (high - low) / 2

    high = min([len(arr), high])
    if high <= m:
        return

    work = [None] * (high - low)
    i, j, k = low, m, 0
    print low, m, high
    while i < m and j < high:
        if arr[i] < arr[j]:
            work[k] = arr[i]
            k += 1
            i += 1
        else:
            work[k] = arr[j]
            k += 1
            j += 1
    while i < m:
        work[k] = arr[i]
        k += 1
        i += 1
    while j < high:
        work[k] = arr[j]
        k += 1
        j += 1
    arr[low:high] = work[:]


if __name__ == '__main__':
    data = [1, 6, 5, 8, 4, 7, 3, 9, 2]
    merge_sort(data)
    print data
