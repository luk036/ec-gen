from typing import Generator


def sjt2(n: int) -> Generator:
    """
    The function `sjt2` generates all permutations of length `n` using the Steinhaus-Johnson-Trotter
    algorithm.

    :param n: The parameter `n` represents the number of elements in the permutation
    :type n: int
    :return: The function `sjt2` is a generator function, which means it yields values instead of
             returning them. It generates all permutations of length `n` using the Steinhaus-Johnson-Trotter
             algorithm. Each permutation is represented as a list of integers.
    """
    if n == 2:
        yield [0, 1]
        yield [1, 0]  # tricky part: return to the origin
        return

    gen = sjt2(n - 1)
    up = range(n)
    down = range(n - 1, -1, -1)

    for pi in gen:
        for i in down:  # downward
            yield pi[:i] + [n - 1] + pi[i:]
        pi = next(gen)
        for i in up:  # upward
            yield pi[:i] + [n - 1] + pi[i:]
