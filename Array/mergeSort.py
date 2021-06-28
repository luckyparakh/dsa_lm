# TC: O(n log n)
# SC: O(n)
import unittest
import logging

logging.basicConfig(level=logging.INFO)


def merge(left, right):
    l = 0
    r = 0
    arr = []
    while (l < len(left)) and (r < len(right)):
        if left[l] < right[r]:
            arr.append(left[l])
            l += 1
        else:
            arr.append(right[r])
            r += 1
    if l < len(left):
        while l < len(left):
            arr.append(left[l])
            l += 1
    if r < len(right):
        while r < len(right):
            arr.append(right[r])
            r += 1
    return arr


def mergeSortFinal(arr, high, low=0):
    if len(arr) < 2:
        return arr
    mid = low + (high - low) // 2
    logging.debug(mid)
    arr_left = arr[:mid + 1]
    logging.debug(arr_left)
    arr_right = arr[mid + 1:]
    logging.debug(arr_right)
    arr_left = mergeSortFinal(arr_left, len(arr_left) - 1)
    arr_right = mergeSortFinal(arr_right, len(arr_right) - 1)
    return merge(arr_left, arr_right)


class Test(unittest.TestCase):
    def test_merge1(self):
        actual = merge([1, 3, 4, 5, 7], [2, 3, 6])
        expected = [1, 2, 3, 3, 4, 5, 6, 7]
        self.assertEqual(actual, expected)

    def test_merge2(self):
        actual = merge([1, 2, 3], [4, 5, 6])
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(actual, expected)

    def test_merge3(self):
        actual = merge([4, 5, 6], [1, 2, 3])
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(actual, expected)

    def test_merge4(self):
        actual = merge([1, 3, 6], [2, 4, 5, 7])
        expected = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(actual, expected)

    def test_merge_sort1(self):
        arr = [8, 4, 3, 12, 25, 6, 13, 10]
        actual = mergeSortFinal(arr, len(arr) - 1)
        expected = [3, 4, 6, 8, 10, 12, 13, 25]
        self.assertEqual(actual, expected)

    def test_merge_sort2(self):
        arr = [12, 11, 13, 5, 6, 7]
        actual = mergeSortFinal(arr, len(arr) - 1)
        expected = [5, 6, 7, 11, 12, 13]
        self.assertEqual(actual, expected)

    def test_merge_sort3(self):
        arr = [38, 27, 43, 3, 9, 82, 10]
        actual = mergeSortFinal(arr, len(arr) - 1)
        expected = [3, 9, 10, 27, 38, 43, 82]
        self.assertEqual(actual, expected)

    def test_merge_sort4(self):
        arr = [3, 2, 1, 4]
        actual = mergeSortFinal(arr, len(arr) - 1)
        expected = [1, 2, 3, 4]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
