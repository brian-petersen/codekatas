import re
from dataclasses import dataclass


_SPLIT_PATTERN = re.compile(r'\s+')
_VALID_LINE_PATTERN = re.compile(r'^\s+\d')


@dataclass
class Data:
    label: str
    a: int
    b: int


def parse_file(file_path, parts_chooser):
    with open(file_path) as file:
        lines = file.readlines()
        lines = list(filter(_is_valid_line, lines))

    return [_parse_line(line, parts_chooser) for line in lines]


def _is_valid_line(line):
    return _VALID_LINE_PATTERN.match(line) is not None


def _parse_line(line, parts_chooser):
    parts = _SPLIT_PATTERN.split(line.strip())

    (label, a, b) = parts_chooser(parts)

    return Data(label, a, b)


def pick_by_smallest_spread(data_points):
    return min(data_points, key=_data_spread)


def _data_spread(data):
    return abs(data.a - data.b)
