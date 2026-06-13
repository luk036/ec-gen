"""
Ehrlich-Hopcroft-Reingold (EHR) Permutation Generator

This module implements the Ehrlich-Hopcroft-Reingold algorithm for generating
all permutations of a set. Each successive permutation is obtained by swapping
the first element with some other element, making it an efficient minimal-change
order.

The function `ehr_gen` takes an integer n and yields integers representing the
index to swap with the first element (index 0) to produce each new permutation.

The algorithm maintains two lists:
  - perm: represents the current permutation (perm[0] is unused)
  - state: tracks the algorithm's progress through the permutation space

Instead of generating and storing all permutations at once, it yields them one
at a time, which saves memory when working with large n.
"""

from typing import Generator


def ehr_gen(n: int) -> Generator[int, None, None]:
    """
    The `ehr_gen` function generates all permutations of a given length
    using the Ehrlich-Hopcroft-Reingold algorithm.

    It yields indices of elements to be swapped with the first element
    (index 0) in each permutation. The algorithm works by maintaining
    two lists, `perm` and `state`, where `perm` represents the current
    permutation and `state` tracks algorithm progress.

    :param n: The parameter `n` represents the number of elements in the
              permutation
    :type n: int

    Examples:
        >>> for i in ehr_gen(4):
        ...     print(f"swap 0 and {i}")
        ...
        swap 0 and 1
        swap 0 and 2
        swap 0 and 1
        swap 0 and 2
        swap 0 and 1
        swap 0 and 3
        swap 0 and 2
        swap 0 and 1
        swap 0 and 2
        swap 0 and 1
        swap 0 and 2
        swap 0 and 3
        swap 0 and 1
        swap 0 and 2
        swap 0 and 1
        swap 0 and 2
        swap 0 and 1
        swap 0 and 3
        swap 0 and 2
        swap 0 and 1
        swap 0 and 2
        swap 0 and 1
        swap 0 and 2
    """
    if n < 2:
        return

    perm = list(range(n))  # perm[0] is never used
    state = [0] * (n + 1)  # state[0] is never used
    while True:
        idx = 1
        while True:
            if state[idx] == idx:
                state[idx] = 0
                idx += 1
            if state[idx] < idx:
                break
        if idx == n:
            break
        state[idx] += 1
        yield perm[idx]
        perm[1:idx] = perm[idx - 1 : 0 : -1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
