"""
Steinhaus-Johnson-Trotter (SJT) Permutation Algorithm

This module implements the Steinhaus-Johnson-Trotter algorithm for generating
all permutations of n elements in minimal-change (adjacent swap) order.

Two variants are provided:

- ``sjt_gen``: Yields swap positions (indices of adjacent elements to swap),
  returning the list to its original order after all permutations.
- ``PlainChanges``: The original "plain changes" formulation, yielding
  swap positions without returning to the original order.

Both functions work recursively: for each permutation of ``n-1`` elements, the
largest element ``n-1`` is moved across all positions, alternating between
upward (left-to-right) and downward (right-to-left) sweeps. Each yielded
value is the index of the first element in the adjacent pair to swap.
"""

from typing import Generator


def sjt_gen(n: int) -> Generator[int, None, None]:
    """
    The function `sjt_gen` generates all permutations of length `n`
    using Steinhaus-Johnson-Trotter algorithm.

    Note:
        The list returns to the original permutations after all swaps.

    :param n: The parameter `n` represents the number of elements
              in the permutation
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

    up_range = range(n - 1)
    down_range = range(n - 2, -1, -1)
    gen = sjt_gen(n - 1)
    for pos in gen:
        for idx in down_range:  # downward
            yield idx
        yield pos + 1
        for idx in up_range:  # upward
            yield idx
        yield next(gen)  # tricky part


def PlainChanges(n: int) -> Generator[int, None, None]:
    """Generate to swaps for Steinhaus-Johnson-Trotter algorithm (original method).

    :param n: The parameter `n` represents the number of elements in the
              permutation
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
    up_range = range(n - 1)
    down_range = range(n - 2, -1, -1)
    recur = PlainChanges(n - 1)
    try:
        while True:
            for pos in down_range:
                yield pos
            yield next(recur) + 1
            for pos in up_range:
                yield pos
            yield next(recur)
    except StopIteration:
        pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
