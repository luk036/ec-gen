from ec_gen.combin_old import emk, emk_gen, comb


def test_emk_gen_odd_odd():
    cnt = 1
    for _ in emk_gen(15, 5):
        cnt += 1
    assert cnt == comb(15, 5)


def test_emk_gen_even_odd():
    cnt = 1
    for _ in emk_gen(16, 5):
        cnt += 1
    assert cnt == comb(16, 5)


def test_emk_gen_odd_even():
    cnt = 1
    for _ in emk_gen(15, 6):
        cnt += 1
    assert cnt == comb(15, 6)


def test_emk_gen_even_even():
    cnt = 1
    for _ in emk_gen(16, 6):
        cnt += 1
    assert cnt == comb(16, 6)


def test_emk_odd():
    cnt = 0
    for _ in emk(5, 2):
        cnt += 1
    assert cnt == comb(5, 2)


def test_emk_even():
    cnt = 0
    for _ in emk(6, 2):
        cnt += 1
    assert cnt == comb(6, 2)
