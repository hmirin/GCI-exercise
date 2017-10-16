import unittest
import main


class Test(unittest.TestCase):

    def test_result_value(self):
        self.assertEqual(main.result, int((1+1000)*1000/2))


if __name__ == '__main__':
    unittest.main()
