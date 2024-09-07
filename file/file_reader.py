from typing import Callable, TypeVar, List

T = TypeVar('T')

class FileReader:

    def __init__(self, path: str, prefix: str|None) -> None:
        if not isinstance(path, str): 
            raise TypeError(f"Expected 'path' to be of type str, got {type(path).__name__} instead.")
        
        if prefix is not None and not isinstance(prefix, str): 
            raise TypeError(f"Expected 'prefix' to be of type str, got {type(prefix).__name__} instead.")

        self._prefix = prefix
        self._path = path

    def get_content_from_file(self, callback: Callable[[str], T]) -> List[T]:
        file_content: List[T] = []

        with open(self._path, 'r') as file:
            file_lines: List[str] = self._transform_file_lines_to_list(file.readlines())
            for line in file_lines:
                content: T = callback(line)
                file_content.append(content)

        return file_content

    @property
    def path(self) -> str:
        return self._path

    @path.setter
    def path(self, new_path: str) -> None:
        self._path = new_path

    def _transform_file_lines_to_list(self, lines: List[str]) -> List[str]:
        result_lines: List[str] = []

        for line in lines:
            if self._contains_whitespace(line):
                result_lines.extend(self._transform_file_lines_to_list(line.split(self._prefix)))
            else:
                result_lines.append(line)

        return result_lines

    def _contains_whitespace(self, s: str) -> bool:
        return self._prefix is not None and s.find(self._prefix) != -1
    