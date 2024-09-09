def NWD(__a: int, __b: int) -> int:
    while __b != 0:
        __a, __b = __b, __a % __b

    return __a    