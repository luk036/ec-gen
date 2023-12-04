from typing import Generator


def brgc_gen(n: int) -> Generator:
    """
    The function `brgc_gen` generates a sequence of binary reflected gray code numbers up to a given
    length `n`.

    :param n: The parameter `n` represents the number of bits in the binary reflected gray code sequence
    :type n: int
    :return: The function `brgc_gen` returns a generator object.

    Examples:
        >>> for i in brgc_gen(4):
        ...     print(f"flip {i}")
        ...
        flip 0
        flip 1
        flip 0
        flip 2
        flip 0
        flip 1
        flip 0
        flip 3
        flip 0
        flip 1
        flip 0
        flip 2
        flip 0
        flip 1
        flip 0
    """
    if n == 1:
        yield 0
        return
    yield from brgc_gen(n - 1)
    yield n - 1
    yield from brgc_gen(n - 1)


def brgc(n: int) -> Generator:
    """
    The function `brgc` generates a binary reflected gray code sequence of length `n`.

    :param n: The parameter `n` represents the number of bits in the binary code
    :type n: int

    Examples:
        >>> s = "◾◽"
        >>> for lst in brgc(4):
        ...     mylst = list(s[i] for i in lst)
        ...     print("".join(mylst))
        ...
        ◾◾◾◾
        ◽◾◾◾
        ◽◽◾◾
        ◾◽◾◾
        ◾◽◽◾
        ◽◽◽◾
        ◽◾◽◾
        ◾◾◽◾
        ◾◾◽◽
        ◽◾◽◽
        ◽◽◽◽
        ◾◽◽◽
        ◾◽◾◽
        ◽◽◾◽
        ◽◾◾◽
        ◾◾◾◽
    """
    lst = list(0 for _ in range(n))
    yield lst
    for i in brgc_gen(n):
        lst[i] = 1 - lst[i]  # flip
        yield lst


if __name__ == "__main__":
    import doctest

    doctest.testmod()
