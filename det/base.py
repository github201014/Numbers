from ..matrix.square import SquareMatrix
class DetBase(object):
    args: SquareMatrix
    def __init__(self, args: SquareMatrix | list[list[int | float]]):
        if not isinstance(args, SquareMatrix):
            args = SquareMatrix(args)
        self.args = args

    @staticmethod
    def __minor__(_matrix, i, j):
        return [row[:j] + row[j + 1:] for row in (_matrix[:i] + _matrix[i + 1:])]

    def __main__(self, _matrix: list[list[int | float]]) -> int | float:
        if len(_matrix) == 1:
            return _matrix[0][0]
        if len(_matrix) == 2:
            return _matrix[0][0] * _matrix[1][1] - _matrix[0][1] * _matrix[1][0]
        det = 0
        for c in range(len(_matrix)):
            det += ((-1) ** c) * _matrix[0][c] * self.__main__(self.__minor__(_matrix, 0, c))
        return det

    def value(self):
        return self.__main__(self.args.args)

    def matrix(self):
        return SquareMatrix(self.args.args)

    def __int__(self):
        return int(self.value())

    def __float__(self):
        return float(self.value())

    def __str__(self):
        return str(self.value())

    def __repr__(self):
        return str(self.value())

