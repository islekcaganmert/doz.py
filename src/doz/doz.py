def from_str(value: str) -> list:
    ret = []
    it = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'X', '↋']
    for i in value:
        if i not in it:
            raise ValueError("invalid literal for 'doz': '" + value + "'")
        ret += [it.index(i)]
    return ret


def from_int(value: int) -> list:
    bases = [1]
    while bases[0] < value:
        bases = [bases[0] * 12] + bases
    ret = []
    for i in bases:
        ret += [value // i]
        value = value % i
    while ret[0] == 0:
        ret.pop(0)
    return ret


def doz_repr(val: list[int]) -> str:
    it = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'X', '↋']
    ret = ''
    for i in val:
        ret += it[i]
    return ret


class doz:
    def __init__(self, value: any) -> None:
        if isinstance(value, str):
            self._val = from_str(value)
        elif isinstance(value, int):
            self._val = from_int(value)
        elif isinstance(value, float):
            raise TypeError("did you mean 'dfz' instead of 'doz'?")
        elif hasattr(value, '__doz__'):
            ret = value.__doz__()
            if type(ret).__name__ != 'doz':
                raise TypeError("'__doz__' must return 'doz', not " + type(ret).__name__)
            self.__dict__ = ret.__dict__
        else:
            raise TypeError(f"'value' must be 'str', 'int', or 'doz' convertable type, not '{type(value).__name__}'")

    def __repr__(self) -> str:
        return doz_repr(self._val)

    def __str__(self) -> str:
        return repr(self)

    def __int__(self) -> int:
        t = list(reversed(self._val))
        o = -1
        r = 0
        for i in t:
            o += 1
            r += (12 ** o) * i
        return r

    def __float__(self) -> float:
        return float(int(self))

    def __add__(self, other):
        if hasattr(other, '__int__'):
            return doz(int(self) + int(other))
        raise TypeError("unsupported operand type(s) for +")

    def __sub__(self, other):
        if hasattr(other, '__int__'):
            return doz(int(self) - int(other))
        raise TypeError("unsupported operand type(s) for -")

    def __mul__(self, other):
        if hasattr(other, '__int__'):
            return doz(int(self) * int(other))
        raise TypeError("unsupported operand type(s) for *")

    def __floordiv__(self, other):
        if hasattr(other, '__int__'):
            return doz(int(self) // int(other))
        raise TypeError("unsupported operand type(s) for //")

    def __mod__(self, other):
        if hasattr(other, '__int__'):
            return doz(int(self) % int(other))
        raise TypeError("unsupported operand type(s) for %")

    def __pow__(self, other):
        if hasattr(other, '__int__'):
            return doz(int(self) ** int(other))
        raise TypeError("unsupported operand type(s) for **")

    def __eq__(self, other):
        if hasattr(other, '__int__'):
            return int(self) == int(other)
        raise TypeError("unsupported operand type(s) for ==")

    def __lt__(self, other):
        if hasattr(other, '__int__'):
            return int(self) < int(other)
        raise TypeError("unsupported operand type(s) for <")

    def __le__(self, other):
        if hasattr(other, '__int__'):
            return int(self) <= int(other)
        raise TypeError("unsupported operand type(s) for <=")

    def __gt__(self, other):
        if hasattr(other, '__int__'):
            return int(self) > int(other)
        raise TypeError("unsupported operand type(s) for >")

    def __ge__(self, other):
        if hasattr(other, '__int__'):
            return int(self) >= int(other)
        raise TypeError("unsupported operand type(s) for >=")

    def __ne__(self, other):
        if hasattr(other, '__int__'):
            return int(self) != int(other)
        raise TypeError("unsupported operand type(s) for !=")
