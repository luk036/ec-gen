from math import factorial

from ec_gen.ehr import ehr_gen
from ec_gen.sjt import PlainChanges, sjt_gen
from ec_gen.sjt_list import sjt2


def test_sjt_gen_odd():
    cnt = 0  # start from 0
    for _ in sjt_gen(5):
        cnt += 1
    assert cnt == factorial(5)


def test_sjt_gen_even():
    cnt = 0  # start from 0
    for _ in sjt_gen(6):
        cnt += 1
    assert cnt == factorial(6)


def test_sjt():
    fruits = list("🍉🍌🍇🍏")
    perm = fruits.copy()
    for x in sjt_gen(4):
        perm[x], perm[x + 1] = perm[x + 1], perm[x]
    assert perm == fruits


def test_ehr_gen_odd():
    cnt = 1
    for _ in ehr_gen(5):
        cnt += 1
    assert cnt == factorial(5)


def test_ehr_gen_even():
    cnt = 1
    for _ in ehr_gen(6):
        cnt += 1
    assert cnt == factorial(6)


def test_ehr4():
    perm = list("🍉🍌🍇🍏")
    for x in ehr_gen(4):
        perm[0], perm[x] = perm[x], perm[0]
    assert perm == list("🍏🍌🍇🍉")


def test_ehr5():
    perm = list("🍉🍌🍇🍏🍑")
    for x in ehr_gen(5):
        perm[0], perm[x] = perm[x], perm[0]
    assert perm == list("🍑🍏🍌🍇🍉")


def test_sjt2_odd():
    cnt = 0  # start from 0
    for _ in sjt2(5):
        cnt += 1
    assert cnt == factorial(5)


def test_sjt2_even():
    cnt = 0  # start from 0
    for _ in sjt2(6):
        cnt += 1
    assert cnt == factorial(6)


def test_plain_changes_odd():
    cnt = 1  # start from 1
    for _ in PlainChanges(5):
        cnt += 1
    assert cnt == factorial(5)


def test_plain_changes_even():
    cnt = 1  # start from 1
    for _ in PlainChanges(6):
        cnt += 1
    assert cnt == factorial(6)
