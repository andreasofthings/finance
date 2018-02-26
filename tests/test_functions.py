import unittest

import finance

class TestFinanceFunctions(unittest.TestCase):

    def test_symbols(self):
        self.assertEqual(type(finance.symbols.dax), type(()))


if __name__ == '__main__':
    unittest.main()
