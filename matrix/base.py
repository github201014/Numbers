from .exception import MatrixError
class MatrixBase(object):
    def __init__(self, args: list[list[int | float]]):
        len0 = len(args[0])
        for i in args:
            if len(i) != len0:
                raise MatrixError("False args")
        self.args = args

    def __str__(self):
        STR_I: int = 0
        string = ""
        for i in self.args:
            string += "["
            STR_J: int = 0
            for j in i:
                string += str(j.__float__())
                if STR_J+1 != len(i):
                    string += ", "
                STR_J += 1
            string += "]\n"
            STR_I += 1
        return string

    def __repr__(self):
        return self.__str__()