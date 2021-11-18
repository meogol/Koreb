import unittest


class AppTests(unittest.TestCase):
    def testOne(self):
        a=2
        b=3
        c = a+b

if __name__ == '__main__':
    test = AppTests()
    test.testOne()
