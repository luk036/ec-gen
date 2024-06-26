"""
Set Partition

A set partition of the set [n] = {1,2,3,...,n} is a collection B0,
B1, ... Bj of disjoint subsets of [n] whose union is [n]. Each Bj
is called a block. Below we show the partitions of [4]. The periods
separtate the individual sets so that, for example, 1.23.4 is the
partition {{1},{2,3},{4}}.

  1 block:  1234
  2 blocks: 123.4   124.3   134.2   1.234   12.34   13.24   14.23
  3 blocks: 1.2.34  1.24.3  14.2.3  13.2.4  12.3.4
  4 blocks: 1.2.3.4

Each partition above has its blocks listed in increasing order of
smallest element; thus block 0 contains element 1, block1 contains
the smallest element not in block 0, and so on. A Restricted Growth
string (or RG string) is a sring a[1..n] where a[i] is the block in
which element i occurs. Restricted Growth strings are often called
restricted growth functions. Here are the RG strings corresponding
to the partitions shown above.

  1 block:  0000
  2 blocks: 0001, 0010, 0100, 0111, 0011, 0101, 0110
  3 blocks: 0122, 0121, 0112, 0120, 0102,

...more

Reference:
Frank Ruskey. Simple combinatorial Gray codes constructed by
reversing sublists. Lecture Notes in Computer Science, #762,
201-208. Also downloadable from
http://webhome.cs.uvic.ca/~ruskey/Publications/SimpleGray/SimpleGray.html
"""

from typing import Generator


def stirling2nd2(n: int) -> int:
    """
    The `stirling2nd2` function calculates the Stirling number of the second kind for a given integer
    `n` (k = 2) using a recursive approach.

    :param n: The parameter `n` represents the number of elements in a set
    :type n: int
    :return: the Stirling number of the second kind for the given input n.

    Examples:
        >>> stirling2nd2(5)
        15
    """
    if n < 3:
        return 1
    return 1 + 2 * stirling2nd2(n - 1)


def set_bipart(n: int) -> Generator:
    """
    The function `set_bipart` generates a sequence of moves that partitions a set of size `n` into two
    subsets.

    :param n: The parameter `n` represents the number of elements in the bi-partition
    :type n: int

    Examples:
        >>> n = 5
        >>> b = [0] * n + [1]
        >>> print(b[1:])
        [0, 0, 0, 0, 1]
        >>> for x in set_bipart(n):
        ...     old = b[x]
        ...     b[x] = 1 - b[x]
        ...     print(b[1:], ": Move {} from B{} to B{}".format(x, old, b[x]))
        ...
        [0, 0, 0, 1, 1] : Move 4 from B0 to B1
        [0, 1, 0, 1, 1] : Move 2 from B0 to B1
        [0, 1, 1, 1, 1] : Move 3 from B0 to B1
        [0, 0, 1, 1, 1] : Move 2 from B1 to B0
        [0, 0, 1, 0, 1] : Move 4 from B1 to B0
        [0, 1, 1, 0, 1] : Move 2 from B0 to B1
        [0, 1, 0, 0, 1] : Move 3 from B1 to B0
        [0, 1, 0, 0, 0] : Move 5 from B1 to B0
        [0, 1, 1, 0, 0] : Move 3 from B0 to B1
        [0, 0, 1, 0, 0] : Move 2 from B1 to B0
        [0, 0, 1, 1, 0] : Move 4 from B0 to B1
        [0, 1, 1, 1, 0] : Move 2 from B0 to B1
        [0, 1, 0, 1, 0] : Move 3 from B1 to B0
        [0, 0, 0, 1, 0] : Move 2 from B1 to B0
    """
    yield from gen0(n)


# The lists S(n,k,0) and S(n,k,1) satisfy the following properties.
# 1. Successive RG sequences differ in exactly one position.
# 2. first(S(n,k,0)) = first(S(n,k,1)) = 0^{n-k}0123...(k-1)
# 3. last(S(n,k,0)) = 0^{n-k}12...(k-1)0
# 4. last(S(n,k,1)) = 012...(k-1)0^{n-k}
# Note that first(S'(n,k,p)) = last(S(n,k,p))


def gen0(n: int) -> Generator:
    """S(n,k,0) even k

    The function `gen0` generates a sequence of numbers that satisfy a specific condition.

    :param n: The parameter `n` represents an integer value
    :type n: int
    :return: a generator object.
    """
    if n < 3:
        return
    yield n - 1
    yield from gen1(n - 1)
    yield n
    yield from neg1(n - 1)


def gen1(n: int) -> Generator:
    """S(n,k,1) even k

    The function `gen1` generates a sequence of numbers that satisfy a specific condition.

    :param n: The parameter `n` represents an integer value
    :type n: int
    :return: a generator object.
    """
    if n < 3:
        return
    yield 2
    yield from neg1(n - 1)
    yield n
    yield from gen1(n - 1)


def neg1(n: int) -> Generator:
    """S'(n,k,1) even k

    The function `neg1` generates a sequence of numbers that satisfy a specific condition.

    :param n: The parameter `n` represents an integer value
    :type n: int
    :return: a generator object.
    """
    if n < 3:
        return
    yield from neg1(n - 1)
    yield n
    yield from gen1(n - 1)
    yield 2


if __name__ == "__main__":
    import doctest

    doctest.testmod()
