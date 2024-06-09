from typing import Generator


def ehr_gen(n: int) -> Generator:
    """
    The function `ehr` generates all permutations of a given length using the EHR algorithm.

    The `ehr_gen` function is a generator that generates all permutations of length `n` using the ehr
    algorithm. It yields the indices of the elements to be swapped with the first element (index 0) in
    each permutation. The algorithm works by maintaining two lists, `b` and `c`, where `b` represents
    the current permutation and `c` keeps track of the state of the algorithm. The algorithm iterates
    through the elements of `c` and updates the elements of `b` accordingly to generate all possible
    permutations.

    :param n: The parameter `n` represents the number of elements in the permutation
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
        swap 0 and 3
    """
    b = list(range(n))  # b[0] is never used
    c = [0] * (n + 1)  # c[0] is never used
    while True:
        k = 1
        while True:
            if c[k] == k:
                c[k] = 0
                k += 1
            if c[k] < k:
                break
        if k == n:
            yield b[n - 1]
            break
        c[k] += 1
        yield b[k]
        b[1:k] = b[k - 1 : 0 : -1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
