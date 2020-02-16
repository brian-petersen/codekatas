import re
from dataclasses import dataclass


_SPLIT_PATTERN = re.compile(r'\s+')
_VALID_LINE_PATTERN = re.compile(r'^\s+\d')


@dataclass
class Data:
    name: str
    score_for: int
    score_against: int


def _parse_file(file_path):
    with open(file_path) as file:
        lines = file.readlines()
        lines = list(filter(_is_valid_line, lines))

    return [_parse_line(line) for line in lines]


def _is_valid_line(line):
    return _VALID_LINE_PATTERN.match(line) is not None


def _parse_line(line):
    parts = _SPLIT_PATTERN.split(line.strip())

    name = parts[1]
    score_for = int(parts[6])
    score_against = int(parts[8])

    return Data(name, score_for, score_against)


def _pick_by_smallest_spread(data_points):
    return min(data_points, key=_data_spread)


def _data_spread(data):
    return abs(data.score_for - data.score_against)


if __name__ == '__main__':
    data_points = _parse_file('football.dat')
    smallest_spread = _pick_by_smallest_spread(data_points)

    print(smallest_spread.name)
