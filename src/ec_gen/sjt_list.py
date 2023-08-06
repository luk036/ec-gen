from typing import Generator


def SJT2(n: int) -> Generator:
    """
    The function `SJT2` generates all permutations of length `n` using the Steinhaus-Johnson-Trotter
    algorithm.

    :param n: The parameter `n` represents the number of elements in the permutation
    :type n: int
    :return: The function `SJT2` is a generator function, which means it yields values instead of
    returning them. It generates all permutations of length `n` using the Steinhaus-Johnson-Trotter
    algorithm. Each permutation is represented as a list of integers.
    """
    if n == 2:
        yield [0, 1]
        yield [1, 0]  # tricky part: return to the origin
        return

    gen = SJT2(n - 1)
    for pi in gen:
        for i in range(n - 1, -1, -1):  # downward
            yield pi[:i] + [n - 1] + pi[i:]
        pi = next(gen)
        for i in range(n):  # upward
            yield pi[:i] + [n - 1] + pi[i:]


def main():
    fruits = list("🍉🍌🍇🍏")
    print(" 0 1 2 3")
    for lst in SJT2(4):
        mylst = list(fruits[i] for i in lst)
        print("".join(mylst))


if __name__ == "__main__":
    main()
