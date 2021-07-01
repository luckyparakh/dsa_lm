# https://leetcode.com/problems/sort-colors/
# SC O(1)
# TC O(n) and only one traversal is allowed.
# Array consist of only 0's, 1's and 2's. Write an algorithm to sort  this array in
# O(n) time complexity and O(1) Space complexity with only one traversal.
import unittest


def sortArray(arr):
    start, current = 0, 0
    end = len(arr) - 1
    while current <= end:
        if arr[current] == 0:
            arr[start], arr[current] = arr[current], arr[start]
            start += 1
            current += 1
        elif arr[current] == 2:
            arr[end], arr[current] = arr[current], arr[end]
            end -= 1
        else:
            current += 1
    return arr


class Test(unittest.TestCase):
    def test1(self):
        array = [0, 1, 2, 2, 1, 0]
        actual = sortArray(array)
        expected = [0, 0, 1, 1, 2, 2]
        self.assertEqual(actual, expected)

    def test2(self):
        array = [0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0]
        actual = sortArray(array)
        expected = [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2]
        self.assertEqual(actual, expected)

    def test3(self):
        array = [0]
        actual = sortArray(array)
        expected = [0]
        self.assertEqual(actual, expected)

    def test4(self):
        array = [0, 1, 2]
        actual = sortArray(array)
        expected = [0, 1, 2]
        self.assertEqual(actual, expected)

    def test5(self):
        array = [0, 0, 0]
        actual = sortArray(array)
        expected = [0, 0, 0]
        self.assertEqual(actual, expected)

    def test6(self):
        array = [1, 1, 1]
        actual = sortArray(array)
        expected = [1, 1, 1]
        self.assertEqual(actual, expected)

    def test7(self):
        array = [2, 2, 2]
        actual = sortArray(array)
        expected = [2, 2, 2]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
