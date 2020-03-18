import sys


def _make_array(words, n):
    array = [False for i in range(n)]

    for word in words:
        word = word.strip()
        array[_get_word_index(word, n)] = True

    return array


def _array_contains_word(array, word, n):
    return array[_get_word_index(word, n)]


def _get_word_index(word, n):
    return hash(word) % n


if __name__ == '__main__':
    n = 1_000_000
    wordlist_path = sys.argv[1]

    with open(wordlist_path) as words:
        array = _make_array(words, n)

    with open('test_words.dict') as test_words:
        test_words = [word.strip() for word in test_words.readlines()]

    test_words_found = [1 if _array_contains_word(array, word, n) else 0 for word in test_words]
    ratio_found = sum(test_words_found) / len(test_words_found)

    print(f'Ratio found: {ratio_found}')
