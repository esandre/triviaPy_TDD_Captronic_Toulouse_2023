import unittest


class MyTestCase(unittest.TestCase):
    def test_record(self):
        self.assertEqual(True, False)

    def test_replay(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
