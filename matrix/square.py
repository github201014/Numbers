from . import Matrix
from .exception import SquareMatrixError

class SquareMatrix(Matrix):
    def __init__(self, args: list[list[int | float]]):
        for a in args:
            if len(a) != len(args):
                raise SquareMatrixError("False args")
        super().__init__(args)


