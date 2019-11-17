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

def chop_recursive(value, values, offset=0):
    if len(values) == 0:
        return -1
    elif len(values) == 1 and values[0] != value:
        return -1
    elif len(values) == 1 and values[0] == value:
        return offset

    mid = len(values) // 2

    left = values[0:mid]
    right = values[mid:]

    if value < values[mid]:
        next_values = left
        next_offset = offset
    else:
        next_values = right
        next_offset = len(left) + offset

    return chop_recursive(value, next_values, next_offset)
