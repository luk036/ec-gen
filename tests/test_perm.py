from math import factorial

from ec_gen.ehr import ehr_gen
from ec_gen.sjt import PlainChanges, sjt_gen
from ec_gen.sjt_list import sjt2


def test_sjt_gen_odd() -> None:
    perm = list("🍉🍑🍌🍏🍇")
    for x in sjt_gen(5):
        perm[x], perm[x + 1] = perm[x + 1], perm[x]
    assert perm == list("🍉🍑🍌🍏🍇")


def test_sjt_gen_even() -> None:
    perm = list("🍉🍑🍌🍏🍇🍓")
    for x in sjt_gen(6):
        perm[x], perm[x + 1] = perm[x + 1], perm[x]
    assert perm == list("🍉🍑🍌🍏🍇🍓")


def test_sjt8() -> None:
    perm = list(range(8))
    for x in sjt_gen(8):
        perm[x], perm[x + 1] = perm[x + 1], perm[x]
    assert perm == list(range(8))


def test_ehr4() -> None:
    perm = list("🍉🍌🍇🍏")
    for x in ehr_gen(4):
        perm[0], perm[x] = perm[x], perm[0]
    perm[0], perm[3] = perm[3], perm[0]
    assert perm == list("🍉🍌🍇🍏")


def test_ehr5() -> None:
    perm = list("🍉🍌🍇🍏🍑")
    for x in ehr_gen(5):
        perm[0], perm[x] = perm[x], perm[0]
    assert perm == list("🍑🍏🍌🍇🍉")


def test_ehr6() -> None:
    perm = list("🍉🍑🍌🍏🍇🍓")
    for x in ehr_gen(6):
        perm[0], perm[x] = perm[x], perm[0]
    perm[0], perm[5] = perm[5], perm[0]
    assert perm == list("🍉🍑🍌🍏🍇🍓")


def test_ehr8() -> None:
    perm = list(range(8))
    for x in ehr_gen(8):
        perm[0], perm[x] = perm[x], perm[0]
    perm[0], perm[7] = perm[7], perm[0]
    assert perm == [0, 2, 3, 1, 5, 6, 4, 7]


def test_sjt2_odd() -> None:
    cnt = 0  # start from 0
    for _ in sjt2(5):
        cnt += 1
    assert cnt == factorial(5)


def test_sjt2_even() -> None:
    cnt = 0  # start from 0
    for _ in sjt2(6):
        cnt += 1
    assert cnt == factorial(6)


def test_plain_changes_odd() -> None:
    cnt = 1  # start from 1
    for _ in PlainChanges(5):
        cnt += 1
    assert cnt == factorial(5)


def test_plain_changes_even() -> None:
    cnt = 1  # start from 1
    for _ in PlainChanges(6):
        cnt += 1
    assert cnt == factorial(6)


def test_sjt_gen_3() -> None:
    gen = sjt_gen(3)
    assert list(gen) == [1, 0, 1, 0, 1, 0]


def test_plain_changes_3() -> None:
    gen = PlainChanges(3)
    assert list(gen) == [1, 0, 1, 0, 1]


def test_sjt2() -> None:
    p = list(sjt2(3))
    assert p == [[0, 1, 2], [0, 2, 1], [2, 0, 1], [2, 1, 0], [1, 2, 0], [1, 0, 2]]
