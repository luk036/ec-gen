""" Combinations """
from functools import lru_cache
from typing import Generator


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
    return 1 if k >= n or k <= 0 else comb_recur(n, k)


@lru_cache
def comb_recur(n: int, k: int) -> int:
    n -= 1
    a = 1 if k == 1 else comb_recur(n, k - 1)
    b = 1 if k == n else comb_recur(n, k)
    return a + b


# @lru_cache
# def comb_recur(n: int, k: int) -> int:
#     return comb_recur_a(n - 1, k - 1) + comb_recur_b(n - 1, k)
#
#
# def comb_recur_a(n: int, k: int) -> int:
#     return 1 if k == 0 else comb_recur(n, k)
#
#
# def comb_recur_b(n: int, k: int) -> int:
#     return 1 if k == n else comb_recur(n, k)


def EMK_comb_gen(n: int, k: int) -> Generator:
    """Generate all combinations by homogeneous revoling-door

    The `EMK_comb_gen` function generates combinations (by swapping pairs of integers) using the EMK algorithm.

    :param n: The parameter `n` represents the total number of elements in the set, and `k` represents
    the number of elements to be selected in each combination
    :type n: int
    :param k: The parameter `k` represents the number of elements to be selected in each combination
    :type k: int
    :return: The function `EMK_gen` returns a generator object that yields pairs of integers `(x, y)`.

    Examples:
        >>> for x, y in EMK_comb_gen(6, 3):
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
    if k >= n or k <= 0:
        return
    if k == 1:
        for i in range(n - 1):
            yield (i, i + 1)
        return
    if k % 2 == 0:
        yield from EMK_gen_even(n, k)
    else:
        yield from EMK_gen_odd(n, k)


def EMK_gen_even(n: int, k: int) -> Generator:
    """Generate all combinations by homogeneous revoling-door

    The `EMK_gen_even` function generates combinations (by swapping pairs of integers) using the EMK algorithm.

    :param n: The parameter `n` represents the total number of elements in the set, and `k` represents
    the number of elements to be selected in each combination
    :type n: int
    :param k: The parameter `k` represents the number of elements to be selected in each combination
    :type k: int
    :return: The function `EMK_gen` returns a generator object that yields pairs of integers `(x, y)`.
    """
    if k >= n - 1:
        yield (n - 2, n - 1)
    else:
        yield from EMK_gen_even(n - 1, k)
        yield (n - 2, n - 1)
        if k == 2:
            for i in range(n - 3, 0, -1):
                yield (i, i - 1)
        else:
            yield from EMK_neg_odd(n - 2, k - 1)
    yield (k - 2, n - 2)
    if k != 2:
        yield from EMK_gen_even(n - 2, k - 2)


def EMK_gen_odd(n: int, k: int) -> Generator:
    """Generate all combinations by homogeneous revoling-door

    The `EMK_gen_odd` function generates combinations (by swapping pairs of integers) using the EMK algorithm.

    :param n: The parameter `n` represents the total number of elements in the set, and `k` represents
    the number of elements to be selected in each combination
    :type n: int
    :param k: The parameter `k` represents the number of elements to be selected in each combination
    :type k: int
    :return: The function `EMK_gen_odd` returns a generator object that yields pairs of integers `(x, y)`.
    """
    if k < n - 1:
        yield from EMK_gen_odd(n - 1, k)
        yield (n - 2, n - 1)
        yield from EMK_neg_even(n - 2, k - 1)
    else:
        yield (n - 2, n - 1)
    yield (k - 2, n - 2)
    if k == 3:
        for i in range(n - 3):
            yield (i, i + 1)
    else:
        yield from EMK_gen_odd(n - 2, k - 2)


def EMK_neg_even(n: int, k: int) -> Generator:
    """
    The `EMK_neg_even` function generates combinations (by swapping pairs of integers in reverse order)
    using the EMK algorithm.

    :param n: The parameter `n` represents the total number of elements in the set, and `k` represents
    the number of elements to be selected in each combination
    :type n: int
    :param k: The parameter `k` represents the number of elements to be selected in each combination
    :type k: int
    :return: The function `EMK_gen_even` returns a generator object that yields pairs of integers `(x, y)`.
    """
    if k != 2:
        yield from EMK_neg_even(n - 2, k - 2)
    yield (n - 2, k - 2)
    if k < n - 1:
        if k != 2:
            yield from EMK_gen_odd(n - 2, k - 1)
        else:
            for i in range(n - 3):
                yield (i, i + 1)
        yield (n - 1, n - 2)
        yield from EMK_neg_even(n - 1, k)
    else:
        yield (n - 1, n - 2)


def EMK_neg_odd(n: int, k: int) -> Generator:
    """
    The `EMK_neg_odd` function generates combinations (by swapping pairs of integers in reverse order)
    using the EMK algorithm.

    :param n: The parameter `n` represents the total number of elements in the set, and `k` represents
    the number of elements to be selected in each combination
    :type n: int
    :param k: The parameter `k` represents the number of elements to be selected in each combination
    :type k: int
    :return: The function `EMK_gen_odd` returns a generator object that yields pairs of integers `(x, y)`.
    """
    if k == 3:
        for i in range(n - 3, 0, -1):
            yield (i, i - 1)
    else:
        yield from EMK_neg_odd(n - 2, k - 2)

    yield (n - 2, k - 2)

    if k >= n - 1:
        yield (n - 1, n - 2)
    else:
        yield from EMK_gen_even(n - 2, k - 1)
        yield (n - 1, n - 2)
        yield from EMK_neg_odd(n - 1, k)


def EMK(n: int, k: int, Zero=0, One=1):
    """
    The EMK function generates combinations by swapping pairs of integers using the EMK algorithm.

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
        >>> for s in EMK(6, 3, Zero="◾", One="◽"):
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
    for x, y in EMK_comb_gen(n, k):
        s[x], s[y] = s[y], s[x]
        yield s


if __name__ == "__main__":
    import doctest

    doctest.testmod()
