# doz

Dozenal & Floating-point Dozenal types for Python 3.11+

Simply, defines `doz` the dozenal and `fdz` the floating-point dozenal.

```python3
from doz import doz, fdz

doz("1X")      # Decimal: 22
doz(22)        # Format from int
fdz("X4.E3")   # Decimal: 124.9375
fdz(124.9375)  # Format from float


# A class that supports casting to doz and fdz
class MyClass(object):
    def __init__(self) -> None:
        ...
    
    def __doz__(self) -> doz:
        return doz(...)
    
    def __fdz__(self) -> fdz:
        return fdz(...)


my_class = MyClass()
doz(my_class)
fdz(my_class)
```