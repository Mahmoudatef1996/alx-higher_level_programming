#!/usr/bin/python3
def pow(a, b):
    """ Calculate the power of a number

    Args:
        a: the base number.
        b: the exponent.
    Returns: the result of a raised to the power of b.
    """
    if b == 0:
        return 1
    elif b > 0:
        ans = 1
        for _ in range(b):
            ans *= a
        return ans
    else:
        return 1 / pow(a, -b)
