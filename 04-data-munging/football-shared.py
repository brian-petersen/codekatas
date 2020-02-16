from shared import parse_file, pick_by_smallest_spread


def _parts_chooser(parts):
    name = parts[1]
    score_for = int(parts[6])
    score_against = int(parts[8])

    return (name, score_for, score_against)


if __name__ == '__main__':
    data_points = parse_file('football.dat', _parts_chooser)
    smallest_spread = pick_by_smallest_spread(data_points)

    print(smallest_spread.label)
