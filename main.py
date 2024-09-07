from shortcut.odd_shortcut import OddShortcutNumber
from file.file_reader import FileReader

class Solution:
    __odd_shortcut_number_instance = OddShortcutNumber() 

    def __init__(self, __path: str, __prefix: str | None):
        self.__file_reader_instance = FileReader(__path, __prefix)

    def task_nr2(self):
        file_content = self.__file_reader_instance.get_content_from_file(int)
        count_not_odd_shortcut_number = 0
        max_number = 0

        for number in file_content:
            odd_shortcut_number = self.__odd_shortcut_number_instance.of(number)

            if odd_shortcut_number == 0:
                max_number = max(max_number, number)
                count_not_odd_shortcut_number += 1

        return f"{count_not_odd_shortcut_number} {max_number}"


