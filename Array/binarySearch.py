# Find out if a key exists in the sorted list
# array[left..right] or not using binary search algorithm
import unittest
import logging

logging.basicConfig(level=logging.INFO)


def binarySearch(array, left, right, key):
    # Base condition (when search space exhausts)
    if right < left:
        return -1
    """
    Integer has an upper range of 65535 if it is an unsigned integer.
    Consider case when right is 65530 and left is 3000. 
    Now if mid = (left + right) // 2 then it will cause buffer overflow.
    And this will give wrong output, hence use mid = left + (right - left) // 2
    """
    # To avoid buffer overflow use
    # mid = left + (right - left) // 2
    mid = (left + right) // 2
    logging.debug(mid)
    # Base condition (when key is found)
    if array[mid] == key:
        return mid
    elif array[mid] > key:
        return binarySearch(array, left, mid - 1, key)
    else:
        return binarySearch(array, mid + 1, right, key)


class Test(unittest.TestCase):

    def test_binary_search_1(self):
        actual = binarySearch([2, 5, 6, 8, 9, 10], 0, 5, 5)
        expected = 1
        self.assertEqual(actual, expected)

    def test_binary_search_2(self):
        actual = binarySearch([2, 5, 6, 8, 9, 10], 0, 5, -10)
        expected = -1
        self.assertEqual(actual, expected)

    def test_binary_search_3(self):
        actual = binarySearch([2, 5, 6, 8, 9, 10], 0, 5, 15)
        expected = -1
        self.assertEqual(actual, expected)

    def test_binary_search_4(self):
        actual = binarySearch([3, 4, 5, 6, 7, 8, 9], 0, 6, 4)
        expected = 1
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
