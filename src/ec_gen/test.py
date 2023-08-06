def PlainChanges(n):
    """Generate the swaps for the Steinhaus-Johnson-Trotter algorithm."""
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
    perm = list("🍉🍌🍇🥝")
    n = 4
    tlist = [["🥝" for i in range(24)] for j in range(n)]
    index = 0
    for j in range(n):
        tlist[j][index] = perm[j]
    for x in PlainChanges(n):
        perm[x], perm[x + 1] = perm[x + 1], perm[x]
        index += 1
        for j in range(n):
            tlist[j][index] = perm[j]
    for j in range(n):
        print("".join(tlist[j]))
