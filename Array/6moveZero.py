# https://leetcode.com/problems/move-zeroes/
# TC: O(n) and only one traversal is allowed.
# SC: O(1)
import unittest


def moveZeroes(arr: list) -> list:
    current = 0
    zero_position = 0
    while current < len(arr):
        if arr[current] != 0:
            if zero_position != current:
                arr[zero_position], arr[current] = arr[current], arr[zero_position]
            zero_position += 1
        current += 1
    return arr


class Test(unittest.TestCase):
    def test1(self):
        array = [0, 1, 2, 2, 1, 0]
        actual = moveZeroes(array)
        expected = [1, 2, 2, 1, 0, 0]
        self.assertEqual(actual, expected)

    def test2(self):
        array = [0, 0]
        actual = moveZeroes(array)
        expected = [0, 0]
        self.assertEqual(actual, expected)

    def test3(self):
        array = [0]
        actual = moveZeroes(array)
        expected = [0]
        self.assertEqual(actual, expected)

    def test4(self):
        array = [1, 2, 2, 0, 0]
        actual = moveZeroes(array)
        expected = [1, 2, 2, 0, 0]
        self.assertEqual(actual, expected)

    def test5(self):
        array = [1, 2, 2, 7]
        actual = moveZeroes(array)
        expected = [1, 2, 2, 7]
        self.assertEqual(actual, expected)

    def test6(self):
        array = [0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
        actual = moveZeroes(array)
        expected = [1, 9, 8, 4, 2, 7, 6, 9, 0, 0, 0, 0, 0]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
