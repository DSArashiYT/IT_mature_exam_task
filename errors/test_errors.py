from unittest import main, TestCase
from errors_func import Errors

class ErrorsClassTest(TestCase):
    def setUp(self) -> None:
        self.errorsInstance = Errors()

    def test_raiseTypeError_method(self):
        with self.assertRaises(TypeError) as errorContent1:
            self.errorsInstance.raiseTypeError("age", "", int)
    
        self.assertEqual(errorContent1.exception.args[0], "Expected 'age' to be of type int, got str instead.")

        with self.assertRaises(TypeError) as errorContent2:
            self.errorsInstance.raiseTypeError("salary", 3, float)

        self.assertEqual(errorContent2.exception.args[0], "Expected 'salary' to be of type float, got int instead.")


    def test_raiseTypeError_method_with_invalid_input(self):
        with self.assertRaises(TypeError):
            self.errorsInstance.raiseTypeError(0, "", str)

        with self.assertRaises(TypeError):
            self.errorsInstance.raiseTypeError(0, 0, 0)

        with self.assertRaises(TypeError):
            self.errorsInstance.raiseTypeError("", 0, 0)

    def test_generateTaskErrors_method(self):
        self.assertEqual(self.errorsInstance.generateTaskErrors(1), "This task cannot be executed!\nErrors: ")
        self.assertEqual(self.errorsInstance.generateTaskErrors(1, 2), "This task cannot be executed!\nErrors: 2")
        self.assertEqual(self.errorsInstance.generateTaskErrors(1, 2, 3, 4, 5), "This task cannot be executed!\nErrors: 2\n3\n4\n5")
