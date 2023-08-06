from math import factorial

from ec_gen.ehr import Ehr_gen
from ec_gen.sjt import SJT_gen


def test_SJT_odd():
    cnt = 0  # start from 0
    for _ in SJT_gen(5):
        cnt += 1
    assert cnt == factorial(5)


def test_SJT_even():
    cnt = 0  # start from 0
    for _ in SJT_gen(6):
        cnt += 1
    assert cnt == factorial(6)


def test_Ehr_odd():
    cnt = 1
    for _ in Ehr_gen(5):
        cnt += 1
    assert cnt == factorial(5)


def test_Ehr_even():
    cnt = 1
    for _ in Ehr_gen(6):
        cnt += 1
    assert cnt == factorial(6)
