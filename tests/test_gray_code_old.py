import pytest

from ec_gen.combin_old import comb, emk, emk_gen


@pytest.mark.parametrize(
    "n, k, expected_comb",
    [
        (15, 5, comb(15, 5)),
        (16, 5, comb(16, 5)),
        (15, 6, comb(15, 6)),
        (16, 6, comb(16, 6)),
    ],
)
def test_emk_gen(n, k, expected_comb):
    cnt = 1
    for _ in emk_gen(n, k):
        cnt += 1
    assert cnt == expected_comb

@pytest.mark.parametrize(
    "n, k, expected_comb",
    [
        (5, 2, comb(5, 2)),
        (6, 2, comb(6, 2)),
    ],
)
def test_emk(n, k, expected_comb):
    cnt = 0
    for _ in emk(n, k):
        cnt += 1
    assert cnt == expected_comb
