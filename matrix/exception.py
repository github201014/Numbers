class MatrixError(Exception):
    def __init__(self, msg: str):
        self.msg = msg

    def __str__(self):
        return f"MatrixError: {self.msg}"

class SquareMatrixError(MatrixError):
    def __str__(self):
        return f"SquareMatrixError: {self.msg}"