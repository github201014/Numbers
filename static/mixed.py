from ..matrix.square import SquareMatrix
from ..det import Det

def det(args: SquareMatrix | list[list[int | float]]):
    return Det(args)