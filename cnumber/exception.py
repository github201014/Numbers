class CNumberException(Exception):
    def __init__(self, msg: str):
        self.msg = msg

    def __str__(self):
        return f"CNumberException: {self.msg}"

class INumberException(CNumberException):
    def __str__(self):
        return f"INumberException: {self.msg}"
