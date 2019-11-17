def chop_iterative(value, values):
    left = 0
    right = len(values) - 1

    while left <= right:
        mid = (left + right) // 2

        if values[mid] == value:
            return mid

        elif values[mid] < value:
            left = mid + 1

        else:
            right = mid - 1

    return -1
