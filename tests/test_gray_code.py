from ec_gen.combin import EMK, EMK_comb_gen, comb
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


def test_EMK_gen_odd_odd():
    cnt = 1
    for _ in EMK_comb_gen(15, 5):
        cnt += 1
    assert cnt == comb(15, 5)


def test_EMK_gen_even_odd():
    cnt = 1
    for _ in EMK_comb_gen(16, 5):
        cnt += 1
    assert cnt == comb(16, 5)


def test_EMK_gen_odd_even():
    cnt = 1
    for _ in EMK_comb_gen(15, 6):
        cnt += 1
    assert cnt == comb(15, 6)


def test_EMK_gen_even_even():
    cnt = 1
    for _ in EMK_comb_gen(16, 6):
        cnt += 1
    assert cnt == comb(16, 6)


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
