

from .exception import *
from .base import FractionBase
class Fraction(FractionBase):
    def clone(self):
        fr = Fraction(self.up, self.down)
        return fr

    def __add__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.up * other.down + self.down * other.up,
                            self.down * other.down)
        elif isinstance(other, float):
            return self.value() + other
        elif isinstance(other, int):
            return self.value() + other
        elif isinstance(other, FractionBase):
            raise FractionException("FractionBase is not used to calculate.")
        return other.__add__(self)

    def __radd__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.up * other.down + self.down * other.up,
                            self.down * other.down)
        elif isinstance(other, float):
            return self.value() + other
        elif isinstance(other, int):
            return self.value() + other
        elif isinstance(other, FractionBase):
            raise FractionException("FractionBase is not used to calculate.")
        return other.__radd__(self)

    def __sub__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.up * other.down - self.down * other.up,
                            self.down * other.down)
        elif isinstance(other, float):
            return self.value() - other
        elif isinstance(other, int):
            return self.value() - other
        elif isinstance(other, FractionBase):
            raise FractionException("FractionBase is not used to calculate.")
        return other.__sub__(self)

    def __rsub__(self, other):
        if isinstance(other, Fraction):
            return Fraction(- self.up * other.down + self.down * other.up,
                            self.down * other.down)
        elif isinstance(other, float):
            return - self.value() + other
        elif isinstance(other, int):
            return - self.value() + other
        elif isinstance(other, FractionBase):
            raise FractionException("FractionBase is not used to calculate.")
        return other.__rsub__(self)

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.up * other.up,
                            self.down * other.down)
        elif isinstance(other, float):
            return self.value() * other
        elif isinstance(other, int):
            return self.value() * other
        elif isinstance(other, FractionBase):
            raise FractionException("FractionBase is not used to calculate.")
        return other.__mul__(self)

    def __rmul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.up * other.up,
                            self.down * other.down)
        elif isinstance(other, float):
            return self.value() * other
        elif isinstance(other, int):
            return self.value() * other
        elif isinstance(other, FractionBase):
            raise FractionException("FractionBase is not used to calculate.")
        return other.__rmul__(self)

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.up * other.down,
                            self.down * other.up)
        elif isinstance(other, float):
            return self.value() / other
        elif isinstance(other, int):
            return self.value() / other
        elif isinstance(other, FractionBase):
            raise FractionException("FractionBase is not used to calculate.")
        return other.__truediv__(self)

    def __rtruediv__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.down * other.up,
                            self.up * other.down)
        elif isinstance(other, float):
            return other / self.value()
        elif isinstance(other, int):
            return other / self.value()
        elif isinstance(other, FractionBase):
            raise FractionException("FractionBase is not used to calculate.")
        return other.__rtruediv__(self)

    def __floordiv__(self, other):
        if isinstance(other, Fraction):
            return int(Fraction(self.up * other.down,
                            self.down * other.up).value())
        elif isinstance(other, float):
            return self.value() // other
        elif isinstance(other, int):
            return self.value() // other
        elif isinstance(other, FractionBase):
            raise FractionException("FractionBase is not used to calculate.")
        return other.__floordiv__(self)

    def __rfloordiv__(self, other):
        if isinstance(other, Fraction):
            return int(Fraction(self.down * other.up,
                            self.up * other.down).value())
        elif isinstance(other, float):
            return other // self.value()
        elif isinstance(other, int):
            return other // self.value()
        elif isinstance(other, FractionBase):
            raise FractionException("FractionBase is not used to calculate.")
        return other.__rfloordiv__(self)

    def __mod__(self, other):
        if isinstance(other, Fraction):
            return self.value() % other.value()
        elif isinstance(other, int):
            return self.value() % other
        elif isinstance(other, float):
            return self.value() % other
        elif isinstance(other, FractionBase):
            raise FractionException("FractionBase is not used to calculate.")

    def __rmod__(self, other):
        if isinstance(other, Fraction):
            return other.value() % self.value()
        elif isinstance(other, int):
            return other % self.value()
        elif isinstance(other, float):
            return other % self.value()
        elif isinstance(other, FractionBase):
            raise FractionException("FractionBase is not used to calculate.")

    def __and__(self, other):
        if self.value() and other:
            return True
        else:
            return False

    def __rand__(self, other):
        if self.value() and other:
            return True
        else:
            return False

    def __or__(self, other):
        if self.value() or other:
            return True
        else:
            return False

    def __ror__(self, other):
        if self.value() or other:
            return True
        else:
            return False

    def __pow__(self, power, modulo=None):
        if isinstance(power, Fraction):
            if int(self.value()) == self.value():
                return Fraction(self.up ** power.value(),
                                self.down ** power.value())
            else:
                return self.value() ** power.value()
        elif isinstance(power, int):
            return Fraction(self.up ** power,
                            self.down ** power)
        elif isinstance(power, float):
            return self.value() ** power
        elif isinstance(power, FractionBase):
            raise FractionException("FractionBase is not used to calculate.")
        return power.__pow__(self)

    def __rpow__(self, other):
        if isinstance(other, Fraction):
            if int(self.value()) == self.value() and int(other.value()) == other.value():
                return int(other.value() ** self.value())
            elif int(self.value()) == self.value() and not int(other.value()) == other.value():
                return Fraction(other.up ** self.value(), other.down ** self.value())
            elif not int(self.value()) == self.value():
                return float(other.value() ** self.value())
        elif isinstance(other, int):
            if int(self.value()) == self.value():
                return int(other ** self.value())
            elif not int(self.value()) == self.value():
                return float(other ** self.value())
        elif isinstance(other, float):
            return float(other ** self.value())
        elif isinstance(other, FractionBase):
            raise FractionException("FractionBase is not used to calculate.")
        return other.__rpow__(self)
