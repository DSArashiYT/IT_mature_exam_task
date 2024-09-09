from shortcut.odd_shortcut import OddShortcutNumber, NOT_IS_ODD_SHORTCUT_NUMBER
from file.file_reader import FileReader
from math_methods.functions import NWD
from errors.errors_func import Errors

class Solution:
    __odd_shortcut_number_instance = OddShortcutNumber() 
    __errors = Errors()

    def __init__(self, __path: str, __prefix: str | None):
        self.__file_reader_instance = FileReader(__path, __prefix)

    def task_nr2(self):
        try:
            numbers_from_file = self.__file_reader_instance.get_content_from_file(int)
            count_not_odd_shortcut_number = 0
            max_number = 0

            for number in numbers_from_file:
                odd_shortcut_number = self.__odd_shortcut_number_instance.of(number)

                if odd_shortcut_number == NOT_IS_ODD_SHORTCUT_NUMBER:
                    max_number = max(max_number, number)
                    count_not_odd_shortcut_number += 1

            return f"{count_not_odd_shortcut_number}\n{max_number}"

        except Exception as err:
            print(self.__errors.generateTaskErrors(*err.args))
            return ""
        
    def task_nr3(self):
        EXCEPTED_SCORE = 7

        try:
            numbers_from_file = self.__file_reader_instance.get_content_from_file(int)
            numbers_when_it_is_divided_by_odd_number: list[str] = []

            for number in numbers_from_file:
                odd_shortcut_number = self.__odd_shortcut_number_instance.of(number)
                
                if NWD(number, odd_shortcut_number) == EXCEPTED_SCORE:
                    numbers_when_it_is_divided_by_odd_number.append(str(number))

            return "\n".join(numbers_when_it_is_divided_by_odd_number)

        except Exception as err:
            print(self.__errors.generateTaskErrors(*err.args))
            return ""

    def changePathFileReader(self, path: str):
        if not isinstance(path, str): self.__errors.raiseTypeError("path", path, str)
        self.__file_reader_instance.path = path
