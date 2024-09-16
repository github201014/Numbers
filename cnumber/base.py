from .exception import CNumberException
class CNumberBase(object):
    def __init__(self, re: float = 0, im: float = 0):
        self.im = im
        self.re = re

    def chIm(self, im: float):
        self.im = im

    def chRe(self, re: float):
        self.re = re

    def clone(self):
        num = CNumberBase(self.re, self.im)
        return num

    def modulus(self):
        return float((self.im ** 2 + self.re ** 2) ** 0.5)

    def __str__(self):
        if self.re != 0:
            if self.im < 0:
                return f"{self.re} - {- self.im}i"
            elif self.im > 0:
                return f"{self.re} + {self.im}i"
            elif self.im == 0:
                return f"{self.re}"
        else:
            if self.im < 0:
                return f"- {- self.im}i"
            elif self.im > 0:
                return f"{self.im}i"
            elif self.im == 0:
                return "0"

    def __int__(self):
        raise CNumberException("Int type is not supported.")

    def __float__(self):
        raise CNumberException("Float type is not supported.")

    def __repr__(self):
        return self, self.__class__, self.im, self.re