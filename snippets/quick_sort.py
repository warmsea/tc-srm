# Unstable


def qsort(arr, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1
    if low < high:
        p = partition(arr, low, high)
        qsort(arr, low, p - 1)
        qsort(arr, p + 1, high)


def partition(arr, low, high):
    pivot_index, pivot_value = pivot(arr, low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    store_index = low
    for i in range(low, high):
        if arr[i] <= pivot_value:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1
    arr[store_index], arr[high] = arr[high], arr[store_index]
    return store_index


def pivot(arr, low, high):
    indices = [low, (low + high) / 2, high]
    values = [arr[i] for i in indices]
    max_value = max(values)
    min_value = min(values)
    for i in range(len(indices)):
        if arr[indices[i]] == max_value:
            del indices[i]
            break
    for i in range(len(indices)):
        if arr[indices[i]] == min_value:
            del indices[i]
            break
    return indices[0], arr[indices[0]]


if __name__ == '__main__':
    data = [1, 6, 5, 8, 4, 7, 3, 9, 2]
    qsort(data)
    print data
