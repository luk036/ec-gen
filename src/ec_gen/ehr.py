"""
The ehr_gen function

This code defines a function called ehr_gen that generates permutations using the Ehrlich-Hopcroft-Reingold (EHR) algorithm. A permutation is a way of arranging a set of items in a different order. The purpose of this code is to efficiently generate all possible permutations of a given length.

The function takes one input: an integer n, which represents the number of elements to permute. For example, if n is 3, it will generate permutations for the elements [0, 1, 2].

The output of this function is a generator that yields integers. These integers represent the index of the element that should be swapped with the first element (index 0) to create each new permutation. By following these swap instructions, you can generate all possible permutations of the n elements.

The algorithm achieves its purpose by using two lists: b and c. List b represents the current permutation, while list c keeps track of the algorithm's state. The function enters a loop where it updates these lists according to specific rules, generating a new permutation with each iteration.

The main logic flow involves finding the next element to swap by iterating through the c list. When it finds the right element, it updates c, yields the index from b, and then partially reverses b to set up for the next permutation. This process continues until all permutations have been generated.

An important aspect of this algorithm is its efficiency. Instead of generating and storing all permutations at once, it yields them one at a time. This approach saves memory and allows for processing of permutations as they're generated, which can be very useful when working with large sets of elements.
"""

from typing import Generator


def ehr_gen(n: int) -> Generator:
    """
    The function `ehr` generates all permutations of a given length using the EHR algorithm.

    The `ehr_gen` function is a generator that generates all permutations of length `n` using the ehr
    algorithm. It yields the indices of the elements to be swapped with the first element (index 0) in
    each permutation. The algorithm works by maintaining two lists, `perm` and `state`, where `perm` represents
    the current permutation and `state` keeps track of the state of the algorithm. The algorithm iterates
    through the elements of `state` and updates the elements of `perm` accordingly to generate all possible
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
