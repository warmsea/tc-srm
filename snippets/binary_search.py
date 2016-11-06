def binary_search(sorted_arr, key, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(sorted_arr) - 1

    if low > high:
        return -1

    m = (high + low) / 2
    if sorted_arr[m] > key:
        return binary_search(sorted_arr, key, low, m - 1)
    elif sorted_arr[m] < key:
        return binary_search(sorted_arr, key, m + 1, high)
    else:
        return m


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print binary_search(arr, 5)
    print binary_search(arr, 4)
