from ec_gen.ehr import ehr_gen


def test_ehr_gen_with_n_zero() -> None:
    gen = ehr_gen(0)
    assert list(gen) == []


def test_ehr_gen_with_n_one() -> None:
    gen = ehr_gen(1)
    assert list(gen) == []


def test_ehr_gen_with_n_three() -> None:
    gen = ehr_gen(3)
    assert list(gen) == [1, 2, 1, 2, 1]
