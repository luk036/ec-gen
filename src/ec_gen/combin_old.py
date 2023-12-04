""" Combinations """
from functools import lru_cache
from typing import Generator


@lru_cache
def comb(n: int, k: int) -> int:
    """
    The `comb` function calculates the number of combinations of `k` elements from a set of `n` elements
    using recursion and memoization.

    :param n: The parameter `n` represents the total number of items or elements available for selection
    in the combination
    :type n: int
    :param k: The parameter `k` represents the number of items to choose from the set of `n` items. In
    other words, it represents the size of the combination
    :type k: int
    :return: The function `comb` returns the number of combinations of `n` items taken `k` at a time.

    Examples:
        >>> comb(6, 3)
        20
        >>> comb(6, 4) == comb(6, 2)
        True
        >>> comb(6, 5) == comb(6, 1)
        True
        >>> comb(6, 6) == comb(6, 0)
        True

    """
    if k >= n or k == 0:
        return 1
    return comb(n - 1, k - 1) + comb(n - 1, k)


def emk_gen(n: int, k: int) -> Generator:
    """Generate all combinations by homogeneous revoling-door

    The `emk_gen` function generates combinations (by swapping pairs of integers) using the emk algorithm.

    :param n: The parameter `n` represents the total number of elements in the set, and `k` represents
    the number of elements to be selected in each combination
    :type n: int
    :param k: The parameter `k` represents the number of elements to be selected in each combination
    :type k: int
    :return: The function `emk_gen` returns a generator object that yields pairs of integers `(x, y)`.

    Examples:
        >>> for x, y in emk_gen(6, 3):
        ...     print(f"swap {x} and {y}")
        ...
        swap 2 and 3
        swap 1 and 2
        swap 0 and 1
        swap 3 and 4
        swap 1 and 0
        swap 2 and 1
        swap 1 and 3
        swap 0 and 1
        swap 1 and 2
        swap 4 and 5
        swap 2 and 0
        swap 0 and 1
        swap 3 and 2
        swap 1 and 0
        swap 2 and 1
        swap 1 and 4
        swap 0 and 1
        swap 1 and 2
        swap 2 and 3
    """
    if n <= k or k == 0:
        return
    if k == 1:
        for i in range(n - 1):
            yield (i, i + 1)
    else:
        yield from emk_gen(n - 1, k)
        yield (n - 2, n - 1)
        yield from emk_neg(n - 2, k - 1)
        yield (k - 2, n - 2)
        yield from emk_gen(n - 2, k - 2)


def emk_neg(n: int, k: int) -> Generator:
    """
    The `emk_neg` function generates combinations (by swapping pairs of integers in reverse order)
    using the emk algorithm.

    :param n: The parameter `n` represents the total number of elements in the set, and `k` represents
    the number of elements to be selected in each combination
    :type n: int
    :param k: The parameter `k` represents the number of elements to be selected in each combination
    :type k: int
    :return: The function `emk_gen` returns a generator object that yields pairs of integers `(x, y)`.
    """
    if n <= k or k == 0:
        return
    if k == 1:
        for i in range(n - 1, 0, -1):
            yield (i, i - 1)
    else:
        yield from emk_neg(n - 2, k - 2)
        yield (n - 2, k - 2)
        yield from emk_gen(n - 2, k - 1)
        yield (n - 1, n - 2)
        yield from emk_neg(n - 1, k)


def emk(n: int, k: int, Zero=0, One=1):
    """
    The emk function generates combinations by swapping pairs of integers using the emk algorithm.

    :param n: The parameter `n` represents the total number of elements in the combination. It is an
    integer value
    :type n: int
    :param k: The parameter `k` represents the number of ones in each combination
    :type k: int
    :param Zero: The `Zero` parameter is the value that represents a zero in the generated combinations.
    In the example code, it is set to 0, defaults to 0 (optional)
    :param One: The value that represents a "1" in the combinations generated by the algorithm, defaults
    to 1 (optional)

    Examples:
        >>> for s in emk(6, 3, Zero="◾", One="◽"):
        ...     print("".join(s))
        ...
        ◽◽◽◾◾◾
        ◽◽◾◽◾◾
        ◽◾◽◽◾◾
        ◾◽◽◽◾◾
        ◾◽◽◾◽◾
        ◽◾◽◾◽◾
        ◽◽◾◾◽◾
        ◽◾◾◽◽◾
        ◾◽◾◽◽◾
        ◾◾◽◽◽◾
        ◾◾◽◽◾◽
        ◽◾◾◽◾◽
        ◾◽◾◽◾◽
        ◾◽◽◾◾◽
        ◽◾◽◾◾◽
        ◽◽◾◾◾◽
        ◽◾◾◾◽◽
        ◾◽◾◾◽◽
        ◾◾◽◾◽◽
        ◾◾◾◽◽◽
    """
    s = [One] * k + [Zero] * (n - k)
    yield s
    for x, y in emk_gen(n, k):
        s[x], s[y] = s[y], s[x]
        yield s


if __name__ == "__main__":
    import doctest

    doctest.testmod()
