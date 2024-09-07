from file_reader import FileReader
import unittest

class FileReaderTest(unittest.TestCase):
    def setUp(self):
        self.instance = FileReader("../data/skrot.txt", None)

    def test_get_content_from_file_with_valid_path(self):
        self.assertEqual(self.instance.get_content_from_file(lambda x: x.strip())[0], "28144")
        self.assertEqual(self.instance.get_content_from_file(int)[1], 25976)

    def test_change_path(self):
        self.assertEqual(self.instance.path, "../data/skrot.txt")

        self.instance.path = "../data/skrot_przyklad.txt"
        self.assertEqual(self.instance.path, "../data/skrot_przyklad.txt")

    def test_get_content_from_file_with_invalid_path(self):
        self.instance.path = "./data/skrot_przyklad.txt"

        with self.assertRaises(OSError):
            self.instance.get_content_from_file(str)

    def test_get_content_from_file_with_invalid_callback(self):
        self.instance.path = "../data/skrot_przyklad.txt"

        with self.assertRaises(TypeError):
            self.instance.get_content_from_file("")

        with self.assertRaises(TypeError):
            self.instance.get_content_from_file(23)

    def test_constructor_with_invalid_input(self):
        with self.assertRaises(TypeError):
            FileReader(1, "\n")
        
        with self.assertRaises(TypeError):
            FileReader("", 3)

        with self.assertRaises(TypeError):
            FileReader(2, 3)

if __name__ == "__main__":
    unittest.main()
