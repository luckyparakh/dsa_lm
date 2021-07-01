# https://leetcode.com/problems/search-in-rotated-sorted-array/
# TC: O(logn)
# SC: O(1)
# https://www.youtube.com/watch?v=uufaK2uLnSI&t=1s

import unittest
import logging

logging.basicConfig(level=logging.DEBUG)


def search_rotated_array(arr, start, end, number):
    if end < start:
        return -1
    mid = start + (end - start) // 2
    if arr[mid] == number:
        return mid
    if arr[mid] <= arr[end]:
        if arr[mid] < number <= arr[end]:
            return search_rotated_array(arr, mid + 1, end, number)
        else:
            return search_rotated_array(arr, start, mid - 1, number)
    if arr[start] <= arr[mid]:
        if arr[start] <= number < arr[mid]:
            return search_rotated_array(arr, start, mid - 1, number)
        else:
            return search_rotated_array(arr, mid + 1, end, number)


class Test(unittest.TestCase):

    def test_search_rotated_array1(self):
        actual = search_rotated_array([3, 4, 5, 6, 7, 8, 9, 10, 1, 2], 0, 9, 1)
        expected = 8
        self.assertEqual(actual, expected)

    def test_search_rotated_array2(self):
        actual = search_rotated_array([5, 6, 7, 8, 9, 10, 1, 2, 3], 0, 8, 3)
        expected = 8
        self.assertEqual(actual, expected)

    def test_search_rotated_array3(self):
        actual = search_rotated_array([5, 6, 7, 8, 9, 10, 1, 2, 3], 0, 8, 28)
        expected = -1
        self.assertEqual(actual, expected)

    def test_search_rotated_array4(self):
        actual = search_rotated_array([30, 40, 50, 10, 20], 0, 4, 10)
        expected = 3
        self.assertEqual(actual, expected)

    def test_search_rotated_array5(self):
        actual = search_rotated_array([30], 0, 0, 30)
        expected = 0
        self.assertEqual(actual, expected)

    def test_search_rotated_array6(self):
        actual = search_rotated_array([30, 60], 0, 1, 60)
        expected = 1
        self.assertEqual(actual, expected)

    def test_search_rotated_array7(self):
        actual = search_rotated_array([10, 20, 30, 40, 60], 0, 4, 20)
        expected = 1
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
