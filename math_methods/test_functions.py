from unittest import main, TestCase
from functions import *

class MathFunctionsTest(TestCase):
    def test_NWD(self):
        self.assertEqual(NWD(125125125, 757575), 75)
        self.assertEqual(NWD(125, 75), 25)
        self.assertEqual(NWD(64, 34), 2)
        self.assertEqual(NWD(49, 7), 7)

if __name__ == "__main__":
    main()