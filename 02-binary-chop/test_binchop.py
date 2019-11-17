import unittest

from binchop import chop_iterative


class TestBinChop(unittest.TestCase):
    def test_chop_iterative(self):
        run_tests(self, chop_iterative)


def run_tests(test_case, chop_impl):
    test_case.assertEqual(-1, chop_impl(3, []))
    test_case.assertEqual(-1, chop_impl(3, [1]))
    test_case.assertEqual(0,  chop_impl(1, [1]))

    test_case.assertEqual(0,  chop_impl(1, [1, 3, 5]))
    test_case.assertEqual(1,  chop_impl(3, [1, 3, 5]))
    test_case.assertEqual(2,  chop_impl(5, [1, 3, 5]))
    test_case.assertEqual(-1, chop_impl(0, [1, 3, 5]))
    test_case.assertEqual(-1, chop_impl(2, [1, 3, 5]))
    test_case.assertEqual(-1, chop_impl(4, [1, 3, 5]))
    test_case.assertEqual(-1, chop_impl(6, [1, 3, 5]))

    test_case.assertEqual(0,  chop_impl(1, [1, 3, 5, 7]))
    test_case.assertEqual(1,  chop_impl(3, [1, 3, 5, 7]))
    test_case.assertEqual(2,  chop_impl(5, [1, 3, 5, 7]))
    test_case.assertEqual(3,  chop_impl(7, [1, 3, 5, 7]))
    test_case.assertEqual(-1, chop_impl(0, [1, 3, 5, 7]))
    test_case.assertEqual(-1, chop_impl(2, [1, 3, 5, 7]))
    test_case.assertEqual(-1, chop_impl(4, [1, 3, 5, 7]))
    test_case.assertEqual(-1, chop_impl(6, [1, 3, 5, 7]))
    test_case.assertEqual(-1, chop_impl(8, [1, 3, 5, 7]))


if __name__ == '__main__':
    unittest.main()
