NOT_IS_ODD_SHORTCUT_NUMBER = 0
class OddShortcutNumber: 
    __isNegativeNumber = False
    __oddBase: int = 1
    __inputNumber: int
    __result: int = 0
    
    def of(self, number: int) -> int:
        self.__resetBaseAndResult()
        self.__checkNumber(number)
        self.__saveNumber(number)
        self.__extractOddDigitsOfNumber(10)

        return self.__result * (-1 if self.__isNegativeNumber else 1)

    def __saveNumber(self, number: int) -> None:
        self.__inputNumber = abs(number)

    def __checkNumber(self, __number: int) -> None:
        self.__isNegativeNumber = (__number < 0)

    def __resetBaseAndResult(self) -> None:
        self.__result = 0
        self.__oddBase = 1

    def __extractOddDigitsOfNumber(self, base: int) -> None:
        while self.__inputNumber != 0:
            current_digit: int = self.__inputNumber % base
            
            if current_digit % 2 != 0:  # Sprawdzenie, czy cyfra jest nieparzysta
                self.__result += current_digit * self.__oddBase
                self.__oddBase *= base

            self.__inputNumber //= base  # Skrócone przypisanie dzielenia

    