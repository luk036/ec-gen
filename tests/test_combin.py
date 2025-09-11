import pytest

from ec_gen.combin import comb, emk, emk_comb_gen


def test_comb_with_various_inputs():
    assert comb(10, 3) == 120
    assert comb(10, 0) == 1
    assert comb(10, 10) == 1
    assert comb(5, 2) == 10


def test_comb_with_invalid_input():
    with pytest.raises(TypeError):
        comb(10, "a")


def test_comb_with_negative_input():
    assert comb(-10, 3) == 1
    assert comb(10, -3) == 1


def test_comb_with_large_input():
    assert comb(100, 50) > 10**28


def test_emk_with_zero_k():
    gen = emk(5, 0)
    assert next(gen) == [0, 0, 0, 0, 0]


def test_emk_with_zero_n_and_k():
    gen = emk(0, 0)
    assert next(gen) == []


def test_emk_comb_gen():
    gen = emk_comb_gen(4, 2)
    assert list(gen) == [(1, 2), (0, 1), (2, 3), (1, 0), (0, 2)]


def test_emk():
    gen = emk(4, 2)
    result = ["".join(map(str, p)) for p in gen]
    assert result == ["1100", "1010", "0110", "0101", "1001", "0011"]
