import unittest
from task3.sort import MergeSort


class TestMergeSort(unittest.TestCase):
    def setUp(self) -> None:
        self.list = [9, 3, 3, 6, 8, 5, 4, 6, 3, 7, -11, -123312, -1]
        self.sorted = [-123312, -11, -1, 3, 3, 3, 4, 5, 6, 6, 7, 8, 9]

    def test_sort(self):
        self.assertEqual(MergeSort.run(self.list), self.sorted)

    def test_sort_reverse(self):
        self.assertEqual(MergeSort.run(self.list, reverse=True), self.sorted[::-1])


if __name__ == '__main__':
    unittest.main()
