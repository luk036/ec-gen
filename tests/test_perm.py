from math import factorial

from ec_gen.ehr import Ehr_gen, Ehr
from ec_gen.sjt import SJT_gen, SJT, PlainChanges
from ec_gen.sjt_list import SJT2


def test_SJT_gen_odd():
    cnt = 0  # start from 0
    for _ in SJT_gen(5):
        cnt += 1
    assert cnt == factorial(5)


def test_SJT_gen_even():
    cnt = 0  # start from 0
    for _ in SJT_gen(6):
        cnt += 1
    assert cnt == factorial(6)


def test_SJT_odd():
    cnt = 0  # start from 0
    for _ in SJT(5):
        cnt += 1
    assert cnt == factorial(5)


def test_SJT_even():
    cnt = 0  # start from 0
    for _ in SJT(6):
        cnt += 1
    assert cnt == factorial(6)


def test_Ehr_gen_odd():
    cnt = 1
    for _ in Ehr_gen(5):
        cnt += 1
    assert cnt == factorial(5)


def test_Ehr_gen_even():
    cnt = 1
    for _ in Ehr_gen(6):
        cnt += 1
    assert cnt == factorial(6)


def test_Ehr_odd():
    cnt = 1
    for _ in Ehr(5):
        cnt += 1
    assert cnt == factorial(5)


def test_Ehr_even():
    cnt = 1
    for _ in Ehr(6):
        cnt += 1
    assert cnt == factorial(6)


def test_SJT2_odd():
    cnt = 0  # start from 0
    for _ in SJT2(5):
        cnt += 1
    assert cnt == factorial(5)


def test_SJT2_even():
    cnt = 0  # start from 0
    for _ in SJT2(6):
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
