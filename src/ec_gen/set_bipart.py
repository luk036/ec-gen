"""
Set Bipartition

A set bipartition of the set [n] = {1,2,3,...,n} is a partition into exactly
two non-empty disjoint subsets B0 and B1 whose union is [n]. Each element is
assigned to either block 0 or block 1.

This module generates all 2^{n-1} - 1 non-trivial bipartitions of an n-element
set using a Gray code order where successive bipartitions differ by moving a
single element from one block to the other.

Reference:
Frank Ruskey. Simple combinatorial Gray codes constructed by
reversing sublists. Lecture Notes in Computer Science, #762,
201-208. Also downloadable from
http://webhome.cs.uvic.ca/~ruskey/Publications/SimpleGray/SimpleGray.html
"""

from typing import Generator


def stirling2nd2(num: int) -> int:
    """
    The `stirling2nd2` function calculates the Stirling number of the second kind for a given integer
    `num` (k = 2) using a recursive approach.

    :param num: The parameter `num` represents the number of elements in a set
    :type num: int
    :return: the Stirling number of the second kind for the given input num.

    Examples:
        >>> stirling2nd2(5)
        15
    """
    if num < 3:
        return 1
    return 1 + 2 * stirling2nd2(num - 1)


def set_bipart(num: int) -> Generator[int, None, None]:
    """
    The function `set_bipart` generates a sequence of moves that partitions a set of size `num` into two
    subsets.

    :param num: The parameter `num` represents the number of elements in the bi-partition
    :type num: int

    Examples:
        >>> num = 5
        >>> blocks = [0] * num + [1]
        >>> print(blocks[1:])
        [0, 0, 0, 0, 1]
        >>> for idx in set_bipart(num):
        ...     old_val = blocks[idx]
        ...     blocks[idx] = 1 - blocks[idx]
        ...     print(blocks[1:], ": Move {} from B{} to B{}".format(idx, old_val, blocks[idx]))
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
    yield from gen0(num)


# The lists S(num) and S'(num) satisfy the following properties:
# 1. Successive bipartitions differ in exactly one element.
# 2. first(S(num)) = 0^{num-1}1
# 3. last(S(num)) = 0^{num-1}1
# 4. first(S'(num)) = last(S(num))


def gen0(num: int) -> Generator[int, None, None]:
    """S(num) — forward generator for set bipartitions.

    :param num: The total number of elements in the set
    :type num: int
    :return: a generator yielding element indices to flip between blocks.
    """
    if num < 3:
        return
    yield num - 1
    yield from gen1(num - 1)
    yield num
    yield from neg1(num - 1)


def gen1(num: int) -> Generator[int, None, None]:
    """S'(num) — alternate forward generator for set bipartitions.

    :param num: The total number of elements in the set
    :type num: int
    :return: a generator yielding element indices to flip between blocks.
    """
    if num < 3:
        return
    yield 2
    yield from neg1(num - 1)
    yield num
    yield from gen1(num - 1)


def neg1(num: int) -> Generator[int, None, None]:
    """S'(num) — reverse generator for set bipartitions.

    :param num: The total number of elements in the set
    :type num: int
    :return: a generator yielding element indices to flip between blocks.
    """
    if num < 3:
        return
    yield from neg1(num - 1)
    yield num
    yield from gen1(num - 1)
    yield 2


if __name__ == "__main__":
    import doctest

    doctest.testmod()
