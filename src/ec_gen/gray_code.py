"""
Binary Reflected Gray Code Generator

This module implements the binary reflected Gray code (BRGC), where
successive binary sequences differ by exactly one bit flip.

Two functions are provided:
- `brgc_gen(n)`: Yields the bit positions to flip in Gray code order,
  using a recursive mirrored construction: brgc(n-1), then flip bit n-1,
  then brgc(n-1) again.
- `brgc(n)`: Generates the full Gray code sequence as lists of bits,
  starting from all zeros and applying the flips from brgc_gen.
"""

from typing import Generator


def brgc_gen(n: int) -> Generator[int, None, None]:
    """
    The function `brgc_gen` generates a sequence of binary reflected gray
    code numbers up to a given length `n`.

    :param n: The parameter `n` represents the number of bits in the
              binary reflected gray code sequence
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


def brgc(n: int) -> Generator[list[int], None, None]:
    """
    The function `brgc` generates a binary reflected gray code sequence of
    length `n`.

    :param n: The parameter `n` represents the number of bits in the
              binary code
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
    bits = list(0 for _ in range(n))
    yield bits
    for idx in brgc_gen(n):
        bits[idx] = 1 - bits[idx]  # flip
        yield bits


if __name__ == "__main__":
    import doctest

    doctest.testmod()
