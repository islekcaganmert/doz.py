from doz.helpers import from_int, from_str, doz_repr
from fractions import Fraction


class fdz:
    def __init__(self, value: any) -> None:
        self._pos = 0
        if isinstance(value, str):
            vl = value.split('.')
            if len(vl) != 2:
                raise ValueError("'value' must be a floating-point dozenal")
            self._pos = len(vl[1])
            self._val = from_str(vl[0] + vl[1])
        elif isinstance(value, int):
            self._val = from_int(value)
        elif isinstance(value, float):
            value = Fraction(value)
            while value % 1:
                value *= 12
                self._pos += 1
            self._val = from_int(int(value))
        elif hasattr(value, '__doz__'):
            ret = value.__doz__()
            if type(ret).__name__ != 'doz':
                raise TypeError("'__doz__' must return 'doz', not " + type(ret).__name__)
            self.__dict__ = ret.__dict__
        elif hasattr(value, '__fdz__'):
            ret = value.__fdz__()
            if type(ret).__name__ != 'fdz':
                raise TypeError("'__fdz__' must return 'fdz', not " + type(ret).__name__)
            self.__dict__ = ret.__dict__
        else:
            raise TypeError("'value' must be 'str', 'int', 'float', or 'fdz' convertable type")

    def __repr__(self) -> str:
        ret = doz_repr(self._val)
        if self._pos == 0:
            return f"{ret}.0"
        return f"{ret[:-self._pos]}.{ret[-self._pos:]}"

    def __str__(self) -> str:
        return repr(self)

    def __float__(self) -> float:
        t = list(reversed(self._val))
        o = -self._pos - 1
        r = 0.0
        for i in t:
            o += 1
            r += (12 ** o) * i
        return r

    def __int__(self) -> int:
        return int(float(self))
    
    def __add__(self, other) -> 'fdz':
        if hasattr(other, '__float__'):
            return fdz(float(self) + float(other))
        raise TypeError("unsupported operand type(s) for +")
    
    def __sub__(self, other) -> 'fdz':
        if hasattr(other, '__float__'):
            return fdz(float(self) - float(other))
        raise TypeError("unsupported operand type(s) for -")
    
    def __mul__(self, other) -> 'fdz':
        if hasattr(other, '__float__'):
            return fdz(float(self) * float(other))
        raise TypeError("unsupported operand type(s) for *")
    
    def __floordiv__(self, other) -> 'fdz':
        if hasattr(other, '__float__'):
            return fdz(float(self) // float(other))
        raise TypeError("unsupported operand type(s) for //")
    
    def __mod__(self, other) -> 'fdz':
        if hasattr(other, '__float__'):
            return fdz(float(self) % float(other))
        raise TypeError("unsupported operand type(s) for %")
    
    def __pow__(self, other) -> 'fdz':
        if hasattr(other, '__float__'):
            return fdz(float(self) ** float(other))
        raise TypeError("unsupported operand type(s) for **")
    
    def __eq__(self, other) -> bool:
        if hasattr(other, '__float__'):
            return float(self) == float(other)
        raise TypeError("unsupported operand type(s) for ==")
    
    def __lt__(self, other) -> bool:
        if hasattr(other, '__float__'):
            return float(self) < float(other)
        raise TypeError("unsupported operand type(s) for <")
    
    def __le__(self, other) -> bool:
        if hasattr(other, '__float__'):
            return float(self) <= float(other)
        raise TypeError("unsupported operand type(s) for <=")
    
    def __gt__(self, other) -> bool:
        if hasattr(other, '__float__'):
            return float(self) > float(other)
        raise TypeError("unsupported operand type(s) for >")
    
    def __ge__(self, other) -> bool:
        if hasattr(other, '__float__'):
            return float(self) >= float(other)
        raise TypeError("unsupported operand type(s) for >=")
    
    def __ne__(self, other) -> bool:
        if hasattr(other, '__float__'):
            return float(self) != float(other)
        raise TypeError("unsupported operand type(s) for !=")
