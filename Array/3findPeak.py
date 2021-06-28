# https://leetcode.com/problems/peak-index-in-a-mountain-array/
# One array of integers is given as an input ,which is initially increasing and then decreasing or
# it can be only increasing or decreasing.
# you need to find the maximum value in the array in O(Log n) Time complexity and O(1) Space
import logging
import unittest

logging.basicConfig(level=logging.INFO)


def findPeak(arr):
    start = 0
    end = len(arr)
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return max(arr[0], arr[1])
    mid = start + (end - start) // 2
    if arr[mid - 1] < arr[mid] < arr[mid + 1]:
        return findPeak(arr[mid + 1:])
    elif arr[mid - 1] > arr[mid] > arr[mid + 1]:
        return findPeak(arr[0:mid])
    elif arr[mid - 1] < arr[mid] > arr[mid + 1]:
        return arr[mid]


class Test(unittest.TestCase):
    def test_max1(self):
        arr = [0, 1, 0]
        actual = findPeak(arr)
        expected = 1
        self.assertEqual(actual, expected)

    def test_max2(self):
        arr = [0, 2, 1, 0]
        actual = findPeak(arr)
        expected = 2
        self.assertEqual(actual, expected)

    def test_max3(self):
        arr = [0, 10, 5, 2]
        actual = findPeak(arr)
        expected = 10
        self.assertEqual(actual, expected)

    def test_max4(self):
        arr = [3, 4, 5, 1]
        actual = findPeak(arr)
        expected = 5
        self.assertEqual(actual, expected)

    def test_max5(self):
        arr = [24, 69, 100, 99, 79, 78, 67, 36, 26, 19]
        actual = findPeak(arr)
        expected = 100
        self.assertEqual(actual, expected)

    def test_max6(self):
        arr = [120, 100, 80, 20, 0]
        actual = findPeak(arr)
        expected = 120
        self.assertEqual(actual, expected)

    def test_max7(self):
        arr = [10, 20, 30, 40, 50]
        actual = findPeak(arr)
        expected = 50
        self.assertEqual(actual, expected)

    def test_max8(self):
        arr = [10]
        actual = findPeak(arr)
        expected = 10
        self.assertEqual(actual, expected)

    def test_max9(self):
        arr = [10, 20]
        actual = findPeak(arr)
        expected = 20
        self.assertEqual(actual, expected)

    def test_max9(self):
        arr = [20, 10]
        actual = findPeak(arr)
        expected = 20
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
