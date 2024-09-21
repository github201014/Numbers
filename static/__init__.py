def int_factorial(arg: int) -> int | None:
    """
    整数阶乘
    """
    from .error import FactorialError
    if arg < 0:
        raise FactorialError(f"参数错误：{arg}")
    elif arg == 0 or arg == 1:
        return 1
    elif arg > 1:
        return arg * int_factorial(arg - 1)

def inverse_ordinal_number(arg: list[float | int]) -> int:
    """
    逆序数函数
    """
    inversions = 0
    for i in range(len(arg)):
        for j in range(i+1, len(arg)):
            if arg[i] > arg[j]:
                inversions += 1
    return inversions


