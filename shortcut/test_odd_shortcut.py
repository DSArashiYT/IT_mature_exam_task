from odd_shortcut import OddShortcutNumber
from unittest import main, TestCase

class OddShortcutNumberTest(TestCase):
    def setUp(self):
        self.instance = OddShortcutNumber()
    
    def test_of_method_with_odd_numbers(self):
        self.assertEqual(self.instance.of(135), 135)
        self.assertEqual(self.instance.of(395), 395)
        self.assertEqual(self.instance.of(1), 1)

    def test_of_method_with_mix_numbers(self):
        self.assertEqual(self.instance.of(13522), 135)
        self.assertEqual(self.instance.of(34125), 315)
        self.assertEqual(self.instance.of(24432), 3)

    def test_of_method_with_even_numbers(self):
        self.assertEqual(self.instance.of(22242), 0)
        self.assertEqual(self.instance.of(0), 0)
        self.assertEqual(self.instance.of(222222), 0)

    def test_of_method_with_large_number(self):
        self.assertEqual(self.instance.of(1234567890123456789), 1357913579)
        self.assertEqual(self.instance.of(111112222233221), 11111331)
        self.assertEqual(self.instance.of(22200221112221111333),1111111333)

    def test_of_method_with_negative_number(self):
        self.assertEqual(self.instance.of(-13522), -135)
        self.assertEqual(self.instance.of(-2344), -3)
        self.assertEqual(self.instance.of(-2), 0)

    def test_of_method_with_invalid_input(self):
        with self.assertRaises(TypeError):
            self.instance.of("abc")

        with self.assertRaises(TypeError):
            self.instance.of(None)


if __name__ == "__main__":
    main()