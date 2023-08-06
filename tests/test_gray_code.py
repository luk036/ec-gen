from ec_gen.combin import EMK, EMK_gen, comb
from ec_gen.gray_code import BRGC, BRGC_gen


def test_BRGC_gen_odd():
    cnt = 1
    for _ in BRGC_gen(5):
        cnt += 1
    assert cnt == 2**5


def test_BRGC_gen_even():
    cnt = 1
    for _ in BRGC_gen(6):
        cnt += 1
    assert cnt == 2**6


def test_BRGC_odd():
    cnt = 0
    for _ in BRGC(5):
        cnt += 1
    assert cnt == 2**5


def test_BRGC_even():
    cnt = 0
    for _ in BRGC(6):
        cnt += 1
    assert cnt == 2**6


def test_EMK_gen_odd():
    cnt = 1
    for _ in EMK_gen(5, 3):
        cnt += 1
    assert cnt == comb(5, 3)


def test_EMK_gen_even():
    cnt = 1
    for _ in EMK_gen(6, 3):
        cnt += 1
    assert cnt == comb(6, 3)


def test_EMK_odd():
    cnt = 0
    for _ in EMK(5, 2):
        cnt += 1
    assert cnt == comb(5, 2)


def test_EMK_even():
    cnt = 0
    for _ in EMK(6, 2):
        cnt += 1
    assert cnt == comb(6, 2)
