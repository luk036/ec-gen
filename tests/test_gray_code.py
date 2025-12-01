from ec_gen.gray_code import brgc, brgc_gen


def test_brgc_gen_odd():
    cnt = 1
    for _ in brgc_gen(5):
        cnt += 1
    assert cnt == 2**5


def test_brgc_gen_even():
    cnt = 1
    for _ in brgc_gen(6):
        cnt += 1
    assert cnt == 2**6


def test_brgc_odd():
    cnt = 0
    for _ in brgc(5):
        cnt += 1
    assert cnt == 2**5


def test_brgc_even():
    cnt = 0
    for _ in brgc(6):
        cnt += 1
    assert cnt == 2**6
