from . import CNumber
from .exception import INumberException

class INumber(CNumber):
    def __init__(self, im: float = 0):
        super().__init__(im = im)

    def chRe(self, re: float | None):
        raise NotImplementedError("INumber don't have re")

    def __setattr__(self, key, value):
        if key == "re" and value != 0:
            raise NotImplementedError("INumber don't have re")
        super().__setattr__(key, value)