import unittest

class TestMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 11)

if __name__ == "__main__":
    unittest.main()
