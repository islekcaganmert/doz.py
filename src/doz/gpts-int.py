class Int:
    def __add__(self, other):
        return Int(self.value + self._convert(other))

    def __sub__(self, other):
        return Int(self.value - self._convert(other))

    def __mul__(self, other):
        return Int(self.value * self._convert(other))

    def __floordiv__(self, other):
        return Int(self.value // self._convert(other))

    def __mod__(self, other):
        return Int(self.value % self._convert(other))

    def __pow__(self, other):
        return Int(self.value ** self._convert(other))

    def __eq__(self, other):
        return self.value == self._convert(other)

    def __lt__(self, other):
        return self.value < self._convert(other)

    def __le__(self, other):
        return self.value <= self._convert(other)

    def __gt__(self, other):
        return self.value > self._convert(other)

    def __ge__(self, other):
        return self.value >= self._convert(other)

    def __ne__(self, other):
        return self.value != self._convert(other)

    def __repr__(self):
        return f"Int({self.value})"

    def __str__(self):
        return self._int_to_str(self.value)
