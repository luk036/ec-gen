import pytest

from ec_gen.combin import comb, emk, emk_comb_gen


def test_comb_with_various_inputs() -> None:
    assert comb(10, 3) == 120
    assert comb(10, 0) == 1
    assert comb(10, 10) == 1
    assert comb(5, 2) == 10


def test_comb_with_invalid_input() -> None:
    with pytest.raises(TypeError):
        comb(10, "a")  # type: ignore[arg-type]


def test_comb_with_negative_input() -> None:
    assert comb(-10, 3) == 1
    assert comb(10, -3) == 1


def test_comb_with_large_input() -> None:
    assert comb(100, 50) > 10**28


def test_emk_with_zero_k() -> None:
    gen = emk(5, 0)
    assert next(gen) == [0, 0, 0, 0, 0]


def test_emk_with_zero_n_and_k() -> None:
    gen = emk(0, 0)
    assert next(gen) == []


def test_emk_comb_gen() -> None:
    gen = emk_comb_gen(4, 2)
    assert list(gen) == [(1, 2), (0, 1), (2, 3), (1, 0), (0, 2)]


def test_emk() -> None:
    gen = emk(4, 2)
    result = ["".join(map(str, p)) for p in gen]
    assert result == ["1100", "1010", "0110", "0101", "1001", "0011"]


def test_emk_gen_odd_odd() -> None:
    cnt = 1
    for _ in emk_comb_gen(15, 5):
        cnt += 1
    assert cnt == comb(15, 5)


def test_emk_gen_even_odd() -> None:
    cnt = 1
    for _ in emk_comb_gen(16, 5):
        cnt += 1
    assert cnt == comb(16, 5)


def test_emk_gen_odd_even() -> None:
    cnt = 1
    for _ in emk_comb_gen(15, 6):
        cnt += 1
    assert cnt == comb(15, 6)


def test_emk_gen_even_even() -> None:
    cnt = 1
    for _ in emk_comb_gen(16, 6):
        cnt += 1
    assert cnt == comb(16, 6)


def test_emk_odd() -> None:
    cnt = 0
    for _ in emk(5, 2):
        cnt += 1
    assert cnt == comb(5, 2)


def test_emk_even() -> None:
    cnt = 0
    for _ in emk(6, 2):
        cnt += 1
    assert cnt == comb(6, 2)


def test_emk_comb_gen_edge_cases() -> None:
    """Test edge cases for emk_comb_gen function"""
    # Test k >= n (should return empty generator)
    gen = emk_comb_gen(5, 5)
    assert list(gen) == []

    gen = emk_comb_gen(5, 6)
    assert list(gen) == []

    # Test k <= 0 (should return empty generator)
    gen = emk_comb_gen(5, 0)
    assert list(gen) == []

    gen = emk_comb_gen(5, -1)
    assert list(gen) == []

    # Test k == 1 (should yield adjacent pairs)
    gen = emk_comb_gen(5, 1)
    expected = [(0, 1), (1, 2), (2, 3), (3, 4)]
    assert list(gen) == expected

    # Test k == 1 with n=2 (minimal case)
    gen = emk_comb_gen(2, 1)
    expected = [(0, 1)]
    assert list(gen) == expected
