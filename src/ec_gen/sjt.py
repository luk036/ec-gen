"""Steinhaus-Johnson-Trotter algorithm"""

from typing import Generator


def sjt_gen(n: int) -> Generator:
    """
    The function `sjt_gen` generates all permutations of length `n` using the Steinhaus-Johnson-Trotter
    algorithm.

    Note:
        The list returns to the original permutations after all swaps.

    :param n: The parameter `n` represents the number of elements in the permutation
    :type n: int
    :return: The function `sjt_gen` returns a generator object.

    Examples:
        >>> perm = list("🍉🍌🍇🍏")
        >>> for x in sjt_gen(4):
        ...     print("".join(perm))
        ...     perm[x], perm[x + 1] = perm[x + 1], perm[x]
        ...
        🍉🍌🍇🍏
        🍉🍌🍏🍇
        🍉🍏🍌🍇
        🍏🍉🍌🍇
        🍏🍉🍇🍌
        🍉🍏🍇🍌
        🍉🍇🍏🍌
        🍉🍇🍌🍏
        🍇🍉🍌🍏
        🍇🍉🍏🍌
        🍇🍏🍉🍌
        🍏🍇🍉🍌
        🍏🍇🍌🍉
        🍇🍏🍌🍉
        🍇🍌🍏🍉
        🍇🍌🍉🍏
        🍌🍇🍉🍏
        🍌🍇🍏🍉
        🍌🍏🍇🍉
        🍏🍌🍇🍉
        🍏🍌🍉🍇
        🍌🍏🍉🍇
        🍌🍉🍏🍇
        🍌🍉🍇🍏

        >>> print("".join(perm))
        🍉🍌🍇🍏
    """

    if n == 2:
        yield 0
        yield 0  # tricky part: return to the origin
        return

    up = range(n - 1)
    down = range(n - 2, -1, -1)
    gen = sjt_gen(n - 1)
    for x in gen:
        for i in down:  # downward
            yield i
        yield x + 1
        for i in up:  # upward
            yield i
        yield next(gen)  # tricky part


def PlainChanges(n) -> Generator:
    """Generate the swaps for the Steinhaus-Johnson-Trotter algorithm (original method).

    :param n: The parameter `n` represents the number of elements in the permutation
    :type n: int
    :return: The function `PlainChanges` returns a generator object.

    Examples:
        >>> perm = list("🍉🍌🍇🍏")
        >>> for x in PlainChanges(4):
        ...     print("".join(perm))
        ...     perm[x], perm[x + 1] = perm[x + 1], perm[x]
        ...
        🍉🍌🍇🍏
        🍉🍌🍏🍇
        🍉🍏🍌🍇
        🍏🍉🍌🍇
        🍏🍉🍇🍌
        🍉🍏🍇🍌
        🍉🍇🍏🍌
        🍉🍇🍌🍏
        🍇🍉🍌🍏
        🍇🍉🍏🍌
        🍇🍏🍉🍌
        🍏🍇🍉🍌
        🍏🍇🍌🍉
        🍇🍏🍌🍉
        🍇🍌🍏🍉
        🍇🍌🍉🍏
        🍌🍇🍉🍏
        🍌🍇🍏🍉
        🍌🍏🍇🍉
        🍏🍌🍇🍉
        🍏🍌🍉🍇
        🍌🍏🍉🍇
        🍌🍉🍏🍇

        >>> print("".join(perm))
        🍌🍉🍇🍏
    """
    if n < 1:
        return
    up = range(n - 1)
    down = range(n - 2, -1, -1)
    recur = PlainChanges(n - 1)
    try:
        while True:
            for x in down:
                yield x
            yield next(recur) + 1
            for x in up:
                yield x
            yield next(recur)
    except StopIteration:
        pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
