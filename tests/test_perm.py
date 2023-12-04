from math import factorial

from ec_gen.ehr import ehr, ehr_gen
from ec_gen.sjt import sjt, PlainChanges, sjt_gen
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


def test_sjt_odd():
    cnt = 0  # start from 0
    for _ in sjt(5):
        cnt += 1
    assert cnt == factorial(5)


def test_sjt_even():
    cnt = 0  # start from 0
    for _ in sjt(6):
        cnt += 1
    assert cnt == factorial(6)


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


def test_ehr_odd():
    cnt = 1
    for _ in ehr(5):
        cnt += 1
    assert cnt == factorial(5)


def test_ehr_even():
    cnt = 1
    for _ in ehr(6):
        cnt += 1
    assert cnt == factorial(6)


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
