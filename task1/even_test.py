import unittest
from task1.even import IsEven


class TestIsEven(unittest.TestCase):
    def setUp(self) -> None:
        self.isEven = IsEven()

    def test_isEvenBasic_int(self):
        self.assertEqual(self.isEven.isEvenBasic(2), True)
        self.assertEqual(self.isEven.isEvenBasic(7), False)

    def test_isEvenBasic_float(self):
        self.assertEqual(self.isEven.isEvenBasic(2.0), True)
        self.assertEqual(self.isEven.isEvenBasic(7.0), False)

    def test_isEvenByBit(self):
        self.assertEqual(self.isEven.isEvenByBit(2), True)
        self.assertEqual(self.isEven.isEvenByBit(7), False)

    def test_isEvenBySubtraction_int(self):
        self.assertEqual(self.isEven.isEvenBySubtraction(2), True)
        self.assertEqual(self.isEven.isEvenBySubtraction(7), False)

    def test_isEvenBySubtraction_float(self):
        self.assertEqual(self.isEven.isEvenBySubtraction(2.0), True)
        self.assertEqual(self.isEven.isEvenBySubtraction(7.0), False)


if __name__ == '__main__':
    unittest.main()
