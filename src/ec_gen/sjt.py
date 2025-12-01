"""
Steinhaus-Johnson-Trotter Algorithm

This code implements the Steinhaus-Johnson-Trotter algorithm, which is a method for generating all possible permutations (arrangements) of a set of items. The code provides two main functions: sjt_gen and PlainChanges, both of which generate a sequence of swaps that, when applied to a list, will produce all possible permutations of that list.

The input for both functions is a single integer n, which represents the number of elements in the list to be permuted. For example, if you have a list of 4 items, you would call the function with n=4.

The output of these functions is a generator object. A generator is a special type of function that returns a sequence of values over time, rather than computing them all at once and returning them in a list. In this case, the generator yields a series of integers representing the positions in the list where swaps should occur to create each new permutation.

The algorithm works by recursively generating permutations for smaller lists and then using those to build up permutations for larger lists. It starts with the simplest case (n=2) and builds up from there. The key idea is to move the largest element through all positions in the list, and then recursively permute the remaining elements.

The main logic flow in both functions involves alternating between moving "up" (from left to right in the list) and moving "down" (from right to left). This is achieved using two range objects: up and down. The functions yield the positions where swaps should occur, alternating between these upward and downward movements.

An important aspect of the algorithm is that it generates permutations in a way that each new permutation differs from the previous one by just a single swap of adjacent elements. This property makes it efficient for certain applications.

The code includes example usage in the docstrings, showing how to apply the generated swaps to a list of fruit emojis. This demonstrates that by following the sequence of swaps produced by these functions, you can generate all possible arrangements of the items in your list.

In summary, this code provides a tool for generating all permutations of a list in a systematic and efficient manner, which can be useful in various programming and mathematical applications where you need to consider all possible arrangements of a set of items.
"""

from typing import Generator


def sjt_gen(n: int) -> Generator[int, None, None]:
    """
    The function `sjt_gen` generates all permutations of length `n` using the Steinhaus-Johnson-Trotter
    algorithm.

    Note:
        The list returns to the original permutations after all swaps.

    :param n: The parameter `n` represents the number of elements in the permutation
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


def PlainChanges(n: int) -> Generator[int, None, None]:
    """Generate the swaps for the Steinhaus-Johnson-Trotter algorithm (original method).

    :param n: The parameter `n` represents the number of elements in the permutation
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
    import doctest

    doctest.testmod()
