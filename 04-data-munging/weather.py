import re
from dataclasses import dataclass


_PATTERN = re.compile(r'\s+')


@dataclass
class Data:
    day: int
    max_temp: int
    min_temp: int


def _parse_file(file_path):
    with open(file_path) as file:
        lines = file.readlines()
        lines = lines[2:-1]

    return [_parse_line(line) for line in lines]


def _parse_line(line):
    [day, max_temp, min_temp] = _PATTERN.split(line.strip())[0:3]
    
    day = int(day)
    max_temp = int(_clean_temp(max_temp))
    min_temp = int(_clean_temp(min_temp))

    return Data(day, max_temp, min_temp)


def _clean_temp(value):
    return value.replace('*', '')


def _pick_by_smallest_spread(data_points):
    return min(data_points, key=_data_spread)


def _data_spread(data):
    return abs(data.max_temp - data.min_temp)


if __name__ == '__main__':
    data_points = _parse_file('weather.dat')
    smallest_spread = _pick_by_smallest_spread(data_points)

    print(smallest_spread.day)
