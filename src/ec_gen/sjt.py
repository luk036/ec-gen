""" Steinhaus-Johnson-Trotter algorithm """
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
        >>> for i in sjt_gen(4):
        ...     print("swap {} and {}".format(i, i + 1))
        ...
        swap 2 and 3
        swap 1 and 2
        swap 0 and 1
        swap 2 and 3
        swap 0 and 1
        swap 1 and 2
        swap 2 and 3
        swap 0 and 1
        swap 2 and 3
        swap 1 and 2
        swap 0 and 1
        swap 2 and 3
        swap 0 and 1
        swap 1 and 2
        swap 2 and 3
        swap 0 and 1
        swap 2 and 3
        swap 1 and 2
        swap 0 and 1
        swap 2 and 3
        swap 0 and 1
        swap 1 and 2
        swap 2 and 3
        swap 0 and 1
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


def sjt(n: int) -> Generator:
    """
    The function `sjt` generates all permutations of length `n` using the Steinhaus-Johnson-Trotter
    algorithm.

    :param n: The parameter `n` represents the number of elements in the permutation
    :type n: int
    :return: The function `sjt` returns a generator object.

    Examples:
        >>> fruits = list("🍉🍌🍇🍏")
        >>> for lst in sjt(4):
        ...     mylst = list(fruits[i] for i in lst)
        ...     print("".join(mylst))
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
    """
    perm = list(range(n))
    for x in sjt_gen(n):
        yield perm
        perm[x], perm[x + 1] = perm[x + 1], perm[x]


def PlainChanges(n):
    """Generate the swaps for the Steinhaus-Johnson-Trotter algorithm (original method)."""
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
    fruits = list("ABCD")
    for lst in sjt(4):
        mylst = list(fruits[i] for i in lst)
        print("".join(mylst))
