

class Errors:
    def generateTaskErrors(self, *args: tuple) -> str:
        return f"This task cannot be executed!\nErrors: {'\n'.join(map(str, args[1:]))}"
    
    def raiseTypeError(self, name: str, var, exceptedVar: object) -> str:
        if not isinstance(name, str): self.__raiseTypeErrorExecute("name", name, str)
        if exceptedVar not in (int, float, str): self.__raiseTypeErrorExecute("name", name, object)
        self.__raiseTypeErrorExecute(name, var, exceptedVar)
        

    def __raiseTypeErrorExecute(self, name: str, var, exceptedVar: object):
        raise TypeError(
            f"Expected '{name}' to be of type {exceptedVar.__name__}, got {type(var).__name__} instead."
        )