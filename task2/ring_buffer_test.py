import unittest
from task2.ring_buffer import RingBufferList, RingBufferArray


class TestRingBufferList(unittest.TestCase):
    def setUp(self) -> None:
        self.buffer = RingBufferList(4)
        return

    def test_ring_buffer_list_push_pop(self):
        self.buffer.push(0)
        self.assertEqual(self.buffer.pop(), 0)

    def test_ring_buffer_list_fill_buffer(self):
        self.buffer.push(0)
        self.buffer.push(1)
        self.buffer.push(2)
        self.buffer.push(3)

        self.assertEqual(self.buffer.pop(), 0)
        self.assertEqual(self.buffer.pop(), 1)
        self.assertEqual(self.buffer.pop(), 2)
        self.assertEqual(self.buffer.pop(), 3)

    def test_ring_buffer_list_overfill_buffer(self):
        self.buffer.push(0)
        self.buffer.push(1)
        self.buffer.push(2)
        self.buffer.push(3)
        self.buffer.push(4)
        self.buffer.push(5)

        self.assertEqual(self.buffer.pop(), 4)
        self.assertEqual(self.buffer.pop(), 5)
        self.assertEqual(self.buffer.pop(), 2)
        self.assertEqual(self.buffer.pop(), 3)

    def test_ring_buffer_list_full_overfill_buffer(self):
        self.buffer.push(0)
        self.buffer.push(1)
        self.buffer.push(2)
        self.buffer.push(3)
        self.buffer.push(4)
        self.buffer.push(5)
        self.buffer.push(6)
        self.buffer.push(7)

        self.assertEqual(self.buffer.pop(), 4)
        self.assertEqual(self.buffer.pop(), 5)
        self.assertEqual(self.buffer.pop(), 6)
        self.assertEqual(self.buffer.pop(), 7)

    def test_ring_buffer_list_fast_pop(self):
        self.buffer.push(0)
        self.assertEqual(self.buffer.pop(), 0)

        self.buffer.push(0)
        self.buffer.push(1)

        self.assertEqual(self.buffer.pop(), 0)
        self.assertEqual(self.buffer.pop(), 1)

        self.buffer.push(0)
        self.buffer.push(1)
        self.buffer.push(2)

        self.assertEqual(self.buffer.pop(), 0)
        self.assertEqual(self.buffer.pop(), 1)
        self.assertEqual(self.buffer.pop(), 2)

        self.buffer.push(0)
        self.buffer.push(1)
        self.buffer.push(2)
        self.buffer.push(3)

        self.assertEqual(self.buffer.pop(), 0)
        self.assertEqual(self.buffer.pop(), 1)
        self.assertEqual(self.buffer.pop(), 2)
        self.assertEqual(self.buffer.pop(), 3)

    def test_ring_buffer_list_pop_empty(self):
        self.assertEqual(self.buffer.pop(), None)


class TestRingBufferArray(unittest.TestCase):
    def setUp(self) -> None:
        self.buffer = RingBufferArray(4, 0xffffff)

    def test_ring_buffer_array_push_pop(self):
        self.buffer.push(0)
        self.assertEqual(self.buffer.pop(), 0)

    def test_ring_buffer_array_fill_buffer(self):
        self.buffer.push(0)
        self.buffer.push(1)
        self.buffer.push(2)
        self.buffer.push(3)

        self.assertEqual(self.buffer.pop(), 0)
        self.assertEqual(self.buffer.pop(), 1)
        self.assertEqual(self.buffer.pop(), 2)
        self.assertEqual(self.buffer.pop(), 3)

    def test_ring_buffer_array_overfill_buffer(self):
        self.buffer.push(0)
        self.buffer.push(1)
        self.buffer.push(2)
        self.buffer.push(3)
        self.buffer.push(4)
        self.buffer.push(5)

        self.assertEqual(self.buffer.pop(), 4)
        self.assertEqual(self.buffer.pop(), 5)
        self.assertEqual(self.buffer.pop(), 2)
        self.assertEqual(self.buffer.pop(), 3)

    def test_ring_buffer_array_full_overfill_buffer(self):
        self.buffer.push(0)
        self.buffer.push(1)
        self.buffer.push(2)
        self.buffer.push(3)
        self.buffer.push(4)
        self.buffer.push(5)
        self.buffer.push(6)
        self.buffer.push(7)

        self.assertEqual(self.buffer.pop(), 4)
        self.assertEqual(self.buffer.pop(), 5)
        self.assertEqual(self.buffer.pop(), 6)
        self.assertEqual(self.buffer.pop(), 7)

    def test_ring_buffer_array_fast_pop(self):
        self.buffer.push(0)
        self.assertEqual(self.buffer.pop(), 0)

        self.buffer.push(0)
        self.buffer.push(1)

        self.assertEqual(self.buffer.pop(), 0)
        self.assertEqual(self.buffer.pop(), 1)

        self.buffer.push(0)
        self.buffer.push(1)
        self.buffer.push(2)

        self.assertEqual(self.buffer.pop(), 0)
        self.assertEqual(self.buffer.pop(), 1)
        self.assertEqual(self.buffer.pop(), 2)

        self.buffer.push(0)
        self.buffer.push(1)
        self.buffer.push(2)
        self.buffer.push(3)

        self.assertEqual(self.buffer.pop(), 0)
        self.assertEqual(self.buffer.pop(), 1)
        self.assertEqual(self.buffer.pop(), 2)
        self.assertEqual(self.buffer.pop(), 3)

    def test_ring_buffer_array_pop_empty(self):
        self.assertEqual(self.buffer.pop(), 0xffffff)


if __name__ == '__main__':
    unittest.main()
