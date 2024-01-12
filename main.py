import unittest
from task1 import even_test


def run_even_test():
    suite = unittest.TestLoader().loadTestsFromModule(even_test)
    unittest.TextTestRunner(verbosity=2).run(suite)


def main():
    run_even_test()
    return


if __name__ == '__main__':
    main()
