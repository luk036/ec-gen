"""Combinations Generator

This code is a collection of functions that work with combinations in mathematics.
A combination is a way of selecting items from a larger set where the order
doesn't matter. The main purpose is to calculate the number of possible
combinations and generate all possible combinations for a given set of elements.

The code takes two main inputs: 'n' (total number of elements in a set) and
'k' (how many elements we want to choose). For example, if we have 6
items and want to choose 3 of them, n would be 6 and k would be 3.

Output varies depending on which function is used. Some functions return the total
number of possible combinations, while others generate the actual combinations.

The code achieves its purpose through several different algorithms:
- 'comb' uses recursion and memoization to calculate combinations
- 'emk_comb_gen' uses the "homogeneous revolving-door" algorithm to generate
  all possible combinations by swapping pairs of elements

An important logic flow is how it handles different cases. When generating
combinations, it treats even and odd numbers of elements differently, using
separate functions for each case. This helps the algorithm work efficiently.

The 'emk' function brings everything together. It generates all combinations by
starting with 'k' ones followed by 'n-k' zeros, then repeatedly swapping
elements based on pairs from 'emk_comb_gen'. This allows producing all
possible combinations without storing them all in memory at once.

Overall, this provides a comprehensive toolkit for working with combinations, from
simple counting to generating all possibilities. It's designed to be efficient
and flexible.
"""

from functools import lru_cache
from typing import Generator


def comb(n: int, k: int) -> int:
    """
    The `comb` function calculates the number of combinations of `k` elements from a set of `n` elements
    using recursion and memoization.

    :param n: The parameter `n` represents the total number of items or elements
              available for selection in the combination
    :type n: int
    :param k: The parameter `k` represents the number of items to choose from
              the set of `n` items. In other words, it represents the size
              of the combination
    :type k: int
    :return: The function `comb` returns the number of combinations of `n`
              items taken `k` at a time.

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
    """
    The function `comb_recur` calculates the number of combinations of `k` elements
    from a set of `n` elements using recursion and memoization.

    :param n: The parameter `n` represents the total number of items to choose
              from
    :type n: int
    :param k: The parameter `k` represents the number of elements to be chosen
              from a set of `n` elements. It is used in the calculation of
              the binomial coefficient, which is the number of ways to choose
              `k` elements from a set of `n` elements
    :type k: int
    :return: The function `comb_recur` returns the sum of two values,
              `val_a` and `val_b`.
    """
    n -= 1
    val_a = 1 if k == 1 else comb_recur(n, k - 1)
    val_b = 1 if k == n else comb_recur(n, k)
    return val_a + val_b


def emk_comb_gen(n: int, k: int) -> Generator[tuple[int, int], None, None]:
    """Generate all combinations by homogeneous revoling-door

    The `emk_comb_gen` function generates combinations (by swapping pairs of
    integers) using the emk algorithm.

    :param n: The parameter `n` represents the total number of elements in the
              set, and `k` represents the number of elements to be selected
              in each combination
    :type n: int
    :param k: The parameter `k` represents the number of elements to be
              selected in each combination
    :type k: int
    :return: The function `emk_gen` returns a generator object that yields
              pairs of integers `(x, y)`.

    Examples:
        >>> for x, y in emk_comb_gen(6, 3):
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
        yield from emk_gen_even(n, k)
    else:
        yield from emk_gen_odd(n, k)


def emk_gen_even(n: int, k: int) -> Generator[tuple[int, int], None, None]:
    """Generate all combinations by homogeneous revoling-door

    The `emk_gen_even` function generates combinations (by swapping pairs of
    integers) using the emk algorithm.

    :param n: The parameter `n` represents the total number of elements in the
              set, and `k` represents the number of elements to be selected in
              each combination
    :type n: int
    :param k: The parameter `k` represents the number of elements to be selected
              in each combination
    :type k: int
    :return: The function `emk_gen` returns a generator object that yields pairs
              of integers `(x, y)`.
    """
    if k >= n - 1:
        yield (n - 2, n - 1)
    else:
        yield from emk_gen_even(n - 1, k)
        yield (n - 2, n - 1)
        if k == 2:
            for i in range(n - 3, 0, -1):
                yield (i, i - 1)
        else:
            yield from emk_neg_odd(n - 2, k - 1)
    yield (k - 2, n - 2)
    if k != 2:
        yield from emk_gen_even(n - 2, k - 2)


def emk_gen_odd(n: int, k: int) -> Generator[tuple[int, int], None, None]:
    """Generate all combinations by homogeneous revoling-door

    The `emk_gen_odd` function generates combinations (by swapping pairs of
    integers) using the emk algorithm.

    :param n: The parameter `n` represents the total number of elements in the
              set, and `k` represents the number of elements to be selected
              in each combination
    :type n: int
    :param k: The parameter `k` represents the number of elements to be
              selected in each combination
    :type k: int
    :return: The function `emk_gen_odd` returns a generator object that yields
              pairs of integers `(x, y)`.
    """
    if k < n - 1:
        yield from emk_gen_odd(n - 1, k)
        yield (n - 2, n - 1)
        yield from emk_neg_even(n - 2, k - 1)
    else:
        yield (n - 2, n - 1)
    yield (k - 2, n - 2)
    if k == 3:
        for i in range(n - 3):
            yield (i, i + 1)
    else:
        yield from emk_gen_odd(n - 2, k - 2)


def emk_neg_even(n: int, k: int) -> Generator[tuple[int, int], None, None]:
    """
    The `emk_neg_even` function generates combinations (by swapping pairs of
    integers in reverse order) using the emk algorithm.

    :param n: The parameter `n` represents the total number of elements in
              the set, and `k` represents the number of elements to be
              selected in each combination
    :type n: int
    :param k: The parameter `k` represents the number of elements to be
              selected in each combination
    :type k: int
    :return: The function `emk_gen_even` returns a generator object that
              yields pairs of integers `(x, y)`.
    """
    if k != 2:
        yield from emk_neg_even(n - 2, k - 2)
    yield (n - 2, k - 2)
    if k < n - 1:
        if k != 2:
            yield from emk_gen_odd(n - 2, k - 1)
        else:
            for i in range(n - 3):
                yield (i, i + 1)
        yield (n - 1, n - 2)
        yield from emk_neg_even(n - 1, k)
    else:
        yield (n - 1, n - 2)


def emk_neg_odd(n: int, k: int) -> Generator[tuple[int, int], None, None]:
    """
    The `emk_neg_odd` function generates combinations (by swapping pairs of
    integers in reverse order) using the emk algorithm.

    :param n: The parameter `n` represents the total number of elements in the
              set, and `k` represents the number of elements to be selected
              in each combination
    :type n: int
    :param k: The parameter `k` represents the number of elements to be
              selected in each combination
    :type k: int
    :return: The function `emk_gen_odd` returns a generator object that yields
              pairs of integers `(x, y)`.
    """
    if k == 3:
        for i in range(n - 3, 0, -1):
            yield (i, i - 1)
    else:
        yield from emk_neg_odd(n - 2, k - 2)

    yield (n - 2, k - 2)

    if k >= n - 1:
        yield (n - 1, n - 2)
    else:
        yield from emk_gen_even(n - 2, k - 1)
        yield (n - 1, n - 2)
        yield from emk_neg_odd(n - 1, k)


def emk(n: int, k: int, zero: int = 0, one: int = 1) -> Generator[list, None, None]:
    """
    The emk function generates combinations by swapping pairs of integers using
    the emk algorithm.

    :param n: The parameter `n` represents the total number of elements in
              the combination. It is an integer value
    :type n: int
    :param k: The parameter `k` represents the number of ones in each
              combination
    :type k: int
    :param Zero: The `Zero` parameter is the value that represents a zero
                  in the generated combinations. In the example code, it is
                  set to 0, defaults to 0 (optional)
    :param One: The value that represents a "1" in the combinations
                  generated by the algorithm, defaults to 1 (optional)

    Examples:
        >>> for s in emk(6, 3, zero="◾", one="◽"):
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
    seq = [one] * k + [zero] * (n - k)
    yield seq
    for pos_x, pos_y in emk_comb_gen(n, k):
        seq[pos_x], seq[pos_y] = seq[pos_y], seq[pos_x]
        yield seq


if __name__ == "__main__":
    import doctest

    doctest.testmod()
