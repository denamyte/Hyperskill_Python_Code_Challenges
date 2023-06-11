# tests for the is_even() function
import unittest


class TestIsEven(unittest.TestCase):

    def test_when_output_true(self):
        self.assertTrue(is_even(4))

    def test_when_output_false(self):
        self.assertFalse(is_even(3))


if __name__ == '__main__':
    unittest.main()