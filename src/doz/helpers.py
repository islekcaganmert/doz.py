def from_str(value: str) -> list:
    ret = []
    it = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'E']
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
    it = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'E']
    ret = ''
    for i in val:
        ret += it[i]
    return ret
