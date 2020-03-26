import unittest

import anagrams


class TestAnagrams(unittest.TestCase):
    def test_find_anagram_sets(self):
        words = [
            'enlist',
            'inlets',
            'listen',
            'silent',
            'not',
            'another',
            'one',
            'ton',
        ]

        expected = [['listen', 'enlist', 'silent', 'inlets'], ['ton', 'not']]
        results = anagrams.find_anagram_sets(words)

        self.assertEqual(expected, results)

if __name__ == '__main__':
    unittest.main()
