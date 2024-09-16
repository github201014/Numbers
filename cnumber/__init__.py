from .base import CNumberBase
from ..fraction import Fraction
from .exception import CNumberException


class CNumber(CNumberBase):
    def __add__(self, other: CNumberBase | int | float | Fraction):
        if isinstance(other, CNumber):
            return CNumber(self.re + other.re,
                           self.im + other.im)
        elif isinstance(other, int):
            return CNumber(self.re + other, self.im)
        elif isinstance(other, float):
            return CNumber(self.re + other, self.im)
        elif isinstance(other, Fraction):
            return CNumber(self.re + other.value(), self.im)
        elif isinstance(other, CNumberBase):
            raise CNumberException("CNumberBase is not used to calculate.")

    def __radd__(self, other: CNumberBase | int | float | Fraction):
        if isinstance(other, CNumber):
            return CNumber(self.re + other.re,
                           self.im + other.im)
        elif isinstance(other, int):
            return CNumber(self.re + other, self.im)
        elif isinstance(other, float):
            return CNumber(self.re + other, self.im)
        elif isinstance(other, Fraction):
            return CNumber(self.re + other.value(), self.im)
        elif isinstance(other, CNumberBase):
            raise CNumberException("CNumberBase is not used to calculate.")

    def __sub__(self, other: CNumberBase | int | float| Fraction):
        if isinstance(other, CNumber):
            return CNumber(self.re - other.re,
                           self.im - other.im)
        elif isinstance(other, int):
            return CNumber(self.re - other, self.im)
        elif isinstance(other, float):
            return CNumber(self.re - other, self.im)
        elif isinstance(other, Fraction):
            return CNumber(self.re - other.value(), self.im)
        elif isinstance(other, CNumberBase):
            raise CNumberException("CNumberBase is not used to calculate.")

    def __rsub__(self, other: CNumberBase | int | float| Fraction):
        if isinstance(other, CNumber):
            return CNumber(- self.re + other.re,
                           - self.im + other.im)
        elif isinstance(other, int):
            return CNumber(- self.re + other, self.im)
        elif isinstance(other, float):
            return CNumber(- self.re + other, self.im)
        elif isinstance(other, Fraction):
            return CNumber(- self.re + other.value(), self.im)
        elif isinstance(other, CNumberBase):
            raise CNumberException("CNumberBase is not used to calculate.")

    def __mul__(self, other: CNumberBase | int | float | Fraction):
        if isinstance(other, CNumber):
            return CNumber(self.re * other.re - self.im * other.im,
                           self.re * other.im + self.im * other.re)
        elif isinstance(other, int):
            return CNumber(self.re * other, self.im * other)
        elif isinstance(other, float):
            return CNumber(self.re * other, self.im * other)
        elif isinstance(other, Fraction):
            return CNumber(self.re * other.value(), self.im * other.value())
        elif isinstance(other, CNumberBase):
            raise CNumberException("CNumberBase is not used to calculate.")

    def __rmul__(self, other: CNumberBase | int | float | Fraction):
        if isinstance(other, CNumber):
            return CNumber(self.re * other.re - self.im * other.im,
                           self.re * other.im + self.im * other.re)
        elif isinstance(other, int):
            return CNumber(self.re * other, self.im * other)
        elif isinstance(other, float):
            return CNumber(self.re * other, self.im * other)
        elif isinstance(other, Fraction):
            return CNumber(self.re * other.value(), self.im * other.value())
        elif isinstance(other, CNumberBase):
            raise CNumberException("CNumberBase is not used to calculate.")

    def __truediv__(self, other: CNumberBase | int | float | Fraction):
        if isinstance(other, CNumber):
            ...
        elif isinstance(other, int):
            ...
        elif isinstance(other, float):
            ...
        elif isinstance(other, Fraction):
            ...
        elif isinstance(other, CNumberBase):
            raise CNumberException("CNumberBase is not used to calculate.")

    def __rtruediv__(self, other: CNumberBase | int | float | Fraction):
        if isinstance(other, CNumber):
            ...
        elif isinstance(other, int):
            ...
        elif isinstance(other, float):
            ...
        elif isinstance(other, Fraction):
            ...
        elif isinstance(other, CNumberBase):
            raise CNumberException("CNumberBase is not used to calculate.")

    def __floordiv__(self, other: CNumberBase | int | float | Fraction):
        if isinstance(other, CNumber):
            ...
        elif isinstance(other, int):
            ...
        elif isinstance(other, float):
            ...
        elif isinstance(other, Fraction):
            ...
        elif isinstance(other, CNumberBase):
            raise CNumberException("CNumberBase is not used to calculate.")

    def __rfloordiv__(self, other: CNumberBase | int | float | Fraction):
        if isinstance(other, CNumber):
            ...
        elif isinstance(other, int):
            ...
        elif isinstance(other, float):
            ...
        elif isinstance(other, Fraction):
            ...
        elif isinstance(other, CNumberBase):
            raise CNumberException("CNumberBase is not used to calculate.")

    def __pow__(self, power: CNumberBase | int | float | Fraction, modulo=None):
        if isinstance(power, CNumber):
            ...
        elif isinstance(power, int):
            ...
        elif isinstance(power, float):
            ...
        elif isinstance(power, Fraction):
            ...
        elif isinstance(power, CNumberBase):
            raise CNumberException("CNumberBase is not used to calculate.")

    def __rpow__(self, other: CNumberBase | int | float | Fraction):
        if isinstance(other, CNumber):
            ...
        elif isinstance(other, int):
            ...
        elif isinstance(other, float):
            ...
        elif isinstance(other, Fraction):
            ...
        elif isinstance(other, CNumberBase):
            raise CNumberException("CNumberBase is not used to calculate.")
