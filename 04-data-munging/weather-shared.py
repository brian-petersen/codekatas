from shared import parse_file, pick_by_smallest_spread


def _parts_chooser(parts):
    [day, max_temp, min_temp] = parts[0:3]

    day = int(day)
    max_temp = int(_clean_temp(max_temp))
    min_temp = int(_clean_temp(min_temp))

    return (day, max_temp, min_temp)


def _clean_temp(value):
    return value.replace('*', '')


if __name__ == '__main__':
    data_points = parse_file('weather.dat', _parts_chooser)
    smallest_spread = pick_by_smallest_spread(data_points)

    print(smallest_spread.label)
