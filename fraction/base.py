class FractionBase(object):
    def __init__(self, up: float, down: float):
        self.up = up
        self.down = down

    def chUp(self, up: float):
        self.up = up

    def chDown(self, down: float):
        self.down = down

    def value(self):
        return self.up / self.down

    def __int__(self):
        return int(self.value())

    def __float__(self):
        return self.value()

    def __bool__(self):
        if self.value() != 0:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.up}/{self.down}"

    def __repr__(self):
        return (f"id::attid:\n"
                f"  self: {id(self)}\n"
                f"  self.up: {id(self.up)}\n"
                f"  self.down: {id(self.down)}\n"
                f"  self.value: {id(self.value())}\n"
                f"id::funcid:\n"
                f"  self.__init__: {id(self.__init__)}\n"
                f"  self.chUp: {id(self.chUp)}\n"
                f"  self.chDown: {id(self.chDown)}\n"
                f"  self.value: {id(self.value)}\n"
                f"value:\n"
                f"  self.up: {self.up}\n"
                f"  self.down: {self.down}\n"
                f"  self.value: {self.value()}\n")