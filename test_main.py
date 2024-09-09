from main import Solution
import unittest

class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.taskInstance = Solution("./data/skrot_przyklad.txt", None)

    def test_task2_with_low_count_numbers(self):
        self.assertEqual(self.taskInstance.task_nr2(), "2\n2428")

    def test_task2_with_a_lot_of_count_numbers(self):
        self.taskInstance.changePathFileReader("./data/skrot.txt")
        self.assertEqual(self.taskInstance.task_nr2(), "18\n28422")

    def test_task2_with_incorect_path(self):
        self.taskInstance.changePathFileReader("./test1.txt")
        self.assertEqual(self.taskInstance.task_nr2(), "")

    def test_task3_with_low_count_numbers(self):
        self.taskInstance.changePathFileReader("./data/skrot2_przyklad.txt")
        self.assertEqual(self.taskInstance.task_nr3(), "4872\n23527")

    def test_task3_with_a_lot_of_count_numbers(self):
        self.taskInstance.changePathFileReader("./data/skrot2.txt")
        self.assertEqual(self.taskInstance.task_nr3(), "784\n14196\n2247\n24087\n3871\n10192")

    def test_task3_with_incorect_path(self):
        self.taskInstance.changePathFileReader("./test1.txt")
        self.assertEqual(self.taskInstance.task_nr3(), "")

    def test_task_constructor_with_invalid_input(self):
        with self.assertRaises(TypeError):
            Solution(2, None)

        with self.assertRaises(TypeError):
            Solution("", 3)

        with self.assertRaises(TypeError):
            Solution(2, 4)

    def test_task_with_invalid_path(self):
        with self.assertRaises(TypeError):
            self.taskInstance.changePathFileReader(2)


if __name__ == "__main__":
    unittest.main()