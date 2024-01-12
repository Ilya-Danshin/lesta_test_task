import unittest
from task1 import even_test
from task2 import ring_buffer_test
from task3 import sort_test


def run_even_tests():
    suite = unittest.TestLoader().loadTestsFromModule(even_test)
    unittest.TextTestRunner(verbosity=2).run(suite)


def run_ring_buffer_tests():
    suite = unittest.TestLoader().loadTestsFromModule(ring_buffer_test)
    unittest.TextTestRunner(verbosity=2).run(suite)


def run_sort_tests():
    suite = unittest.TestLoader().loadTestsFromModule(sort_test)
    unittest.TextTestRunner(verbosity=2).run(suite)


def main():
    run_even_tests()
    run_ring_buffer_tests()
    run_sort_tests()

    return


if __name__ == '__main__':
    main()
