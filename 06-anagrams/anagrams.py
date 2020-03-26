import sys
from itertools import permutations
from timeit import timeit


def find_anagram_sets(words):
    anagram_sets = dict()
    for word in words:
        key = ''.join(sorted(word))
        if key not in anagram_sets:
            anagram_sets[key] = list()
        anagram_sets[key].append(word)

    return [x for x in anagram_sets.values() if len(x) > 1]


def _test_timing(words):
    trials = 10
    total_time = timeit(lambda: find_anagram_sets(words), number=trials)
    average_time = total_time / trials

    print(f'{trials} trials took a total of {total_time} secs')
    print(f'Average time was {average_time} secs')


def _print_anagrams(words):
    anagram_sets = find_anagram_sets(words)
    for anagram_set in anagram_sets:
        print(" ".join(anagram_set))


if __name__ == '__main__':
    words = set()
    for word in open(sys.argv[1]):
        words.add(word.strip().lower())

    _test_timing(words)
    # _print_anagrams(words)
