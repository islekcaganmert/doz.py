from doz.doz import doz as dozBase
from doz.fdz import fdz as fdzBase


class doz(dozBase):
    def __init__(self, value: any) -> None:
        super().__init__(value)

    def __doz__(self) -> 'doz':
        return self

    def __fdz__(self) -> 'fdz':
        return fdz(self._val)


class fdz(fdzBase):
    def __init__(self, value: any) -> None:
        super().__init__(value)

    def __doz__(self) -> 'doz':
        return doz(int(self))

    def __fdz(self) -> 'fdz':
        return self
