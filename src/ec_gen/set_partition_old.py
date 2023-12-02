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
 whcih element i occurs. Restricted Growth strings are often called
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
from functools import lru_cache
from typing import Generator


@lru_cache
def stirling2nd(n: int, k: int) -> int:
    """
    The `stirling2nd` function calculates the Stirling number of the second kind for given values of `n`
    and `k`.

    :param n: The parameter `n` represents the total number of objects or elements in a set
    :type n: int
    :param k: The parameter `k` represents the number of non-empty subsets that need to be formed from a
    set of `n` elements
    :type k: int
    :return: The function `stirling2nd` returns an integer, which is the Stirling number of the second
    kind for the given values of `n` and `k`.

    Examples:
        >>> stirling2nd(5, 2)
        15
    """
    if k >= n or k <= 1:
        return 1
    return stirling2nd(n - 1, k - 1) + k * stirling2nd(n - 1, k)


def set_partition(n: int, k: int) -> Generator:
    """
    The `set_partition` function generates all possible set partitions of a set of size `n` into `k`
    blocks.

    :param n: The parameter `n` represents the total number of elements in the set
    :type n: int
    :param k: The parameter `k` represents the number of blocks in the set partition
    :type k: int

    Examples:
        >>> n, k = 5, 2
        >>> b = [0] * (n - k + 1) + list(range(k))
        >>> print(b[1:])
        [0, 0, 0, 0, 1]
        >>> for x, y in set_partition(n, k):
        ...     old = b[x]
        ...     b[x] = y
        ...     print(b[1:], f": Move {x} from block {old} to {y}")
        ...
        [0, 0, 0, 1, 1] : Move 4 from block 0 to 1
        [0, 1, 0, 1, 1] : Move 2 from block 0 to 1
        [0, 1, 1, 1, 1] : Move 3 from block 0 to 1
        [0, 0, 1, 1, 1] : Move 2 from block 1 to 0
        [0, 0, 1, 0, 1] : Move 4 from block 1 to 0
        [0, 1, 1, 0, 1] : Move 2 from block 0 to 1
        [0, 1, 0, 0, 1] : Move 3 from block 1 to 0
        [0, 1, 0, 0, 0] : Move 5 from block 1 to 0
        [0, 1, 1, 0, 0] : Move 3 from block 0 to 1
        [0, 0, 1, 0, 0] : Move 2 from block 1 to 0
        [0, 0, 1, 1, 0] : Move 4 from block 0 to 1
        [0, 1, 1, 1, 0] : Move 2 from block 0 to 1
        [0, 1, 0, 1, 0] : Move 3 from block 1 to 0
        [0, 0, 0, 1, 0] : Move 2 from block 1 to 0
    """
    if k % 2 == 0:
        yield from GEN0_even(n, k)
    else:
        yield from GEN0_odd(n, k)


# The lists S(n,k,0) and S(n,k,1) satisfy the following properties.
# 1. Successive RG sequences differ in exactly one position.
# 2. first(S(n,k,0)) = first(S(n,k,1)) = 0^{n-k}0123...(k-1)
# 3. last(S(n,k,0)) = 0^{n-k}12...(k-1)0
# 4. last(S(n,k,1)) = 012...(k-1)0^{n-k}
# Note that first(S'(n,k,p)) = last(S(n,k,p))


def GEN0_even(n: int, k: int) -> Generator:
    """S(n,k,0) even k

    The function `GEN0_even` generates a sequence of tuples that satisfy certain conditions based on the
    values of `n` and `k`.

    :param n: The parameter `n` represents the total number of elements in a sequence. It is an integer
    value
    :type n: int
    :param k: The parameter `k` represents the number of elements to be selected from a set of `n`
    elements. It is used in the context of generating even-sized subsets of a set
    :type k: int
    """
    if k > 0 and k < n:
        yield from GEN0_odd(n - 1, k - 1)
        yield (n - 1, k - 1)
        yield from GEN1_even(n - 1, k)
        yield (n, k - 2)
        yield from NEG1_even(n - 1, k)
        for i in range(k - 3, 0, -2):
            yield (n, i)
            yield from GEN1_even(n - 1, k)
            yield (n, i - 1)
            yield from NEG1_even(n - 1, k)


def NEG0_even(n: int, k: int) -> Generator:
    """S'(n,k,0) even k

    The function `NEG0_even` generates a sequence of tuples that satisfy certain conditions based on the
    input parameters `n` and `k`.

    :param n: The parameter `n` represents the total number of elements in a sequence or set. It is an
    integer value
    :type n: int
    :param k: The parameter `k` represents the number of elements to be selected from a set of `n`
    elements. It is used to control the iteration and recursion in the function
    :type k: int
    """
    if k > 0 and k < n:
        for i in range(1, k - 2, 2):
            yield from GEN1_even(n - 1, k)
            yield (n, i)
            yield from NEG1_even(n - 1, k)
            yield (n, i + 1)
        yield from GEN1_even(n - 1, k)
        yield (n, k - 1)
        yield from NEG1_even(n - 1, k)
        yield (n - 1, 0)
        yield from NEG0_odd(n - 1, k - 1)


def GEN1_even(n: int, k: int) -> Generator:
    """S(n,k,1) even k

    Args:
        n (int): [description]
        k (int): [description]

    Yields:
        [type]: [description]
    """
    if k > 1 and k < n:
        yield from GEN1_odd(n - 1, k - 1)
        yield (k, k - 1)
        yield from NEG1_even(n - 1, k)
        yield (n, k - 2)
        yield from GEN1_even(n - 1, k)
        for i in range(k - 3, 0, -2):
            yield (n, i)
            yield from NEG1_even(n - 1, k)
            yield (n, i - 1)
            yield from GEN1_even(n - 1, k)


def NEG1_even(n: int, k: int) -> Generator:
    """S'(n,k,1) even k

    Args:
        n (int): [description]
        k (int): [description]

    Yields:
        [type]: [description]
    """
    if k > 1 and k < n:
        for i in range(1, k - 2, 2):
            yield from NEG1_even(n - 1, k)
            yield (n, i)
            yield from GEN1_even(n - 1, k)
            yield (n, i + 1)
        yield from NEG1_even(n - 1, k)
        yield (n, k - 1)
        yield from GEN1_even(n - 1, k)
        yield (k, 0)
        yield from NEG1_odd(n - 1, k - 1)


def GEN0_odd(n: int, k: int) -> Generator:
    """S(n,k,0) odd k

    Args:
        n (int): [description]
        k (int): [description]

    Yields:
        [type]: [description]
    """
    if k > 2 and k < n:
        yield from GEN1_even(n - 1, k - 1)
        yield (k, k - 1)
        yield from NEG1_odd(n - 1, k)
        for i in range(k - 2, 0, -2):
            yield (n, i)
            yield from GEN1_odd(n - 1, k)
            yield (n, i - 1)
            yield from NEG1_odd(n - 1, k)


# def GEN0_odd(n: int, k: int) -> Generator:
#     ''' S(n,k,0) odd k '''
#     if k > 1 and k < n:
#         yield from GEN1_even(n-1, k-1)
#         yield (k, k-1)
#         even = False
#         for i in range(k-2, -1, -1):
#             yield from GEN1_odd(n-1, k) if even \
#                   else NEG1_odd(n-1, k)
#             yield (n, i)
#             even = ~even
#         yield from NEG1_odd(n-1, k)


def NEG0_odd(n: int, k: int) -> Generator:
    """S'(n,k,0) odd k

    Args:
        n (int): [description]
        k (int): [description]

    Yields:
        [type]: [description]
    """
    if k > 2 and k < n:
        for i in range(1, k - 1, 2):
            yield from GEN1_odd(n - 1, k)
            yield (n, i)
            yield from NEG1_odd(n - 1, k)
            yield (n, i + 1)
        yield from GEN1_odd(n - 1, k)
        yield (k, 0)
        yield from NEG1_even(n - 1, k - 1)


def GEN1_odd(n: int, k: int) -> Generator:
    """S(n,k,1) odd k

    Args:
        n (int): [description]
        k (int): [description]

    Yields:
        [type]: [description]
    """
    if k > 2 and k < n:
        yield from GEN0_even(n - 1, k - 1)
        yield (n - 1, k - 1)
        yield from GEN1_odd(n - 1, k)
        for i in range(k - 2, 0, -2):
            yield (n, i)
            yield from NEG1_odd(n - 1, k)
            yield (n, i - 1)
            yield from GEN1_odd(n - 1, k)


def NEG1_odd(n: int, k: int) -> Generator:
    """S'(n,k,1) odd k

    Args:
        n (int): [description]
        k (int): [description]

    Yields:
        [type]: [description]
    """
    if k > 2 and k < n:
        for i in range(1, k - 1, 2):
            yield from NEG1_odd(n - 1, k)
            yield (n, i)
            yield from GEN1_odd(n - 1, k)
            yield (n, i + 1)
        yield from NEG1_odd(n - 1, k)
        yield (n - 1, 0)
        yield from NEG0_even(n - 1, k - 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
