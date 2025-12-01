import pytest

from ec_gen.set_bipart import set_bipart, stirling2nd2
from ec_gen.set_partition import set_partition, stirling2nd


@pytest.mark.parametrize(
    "n, k, expected_stirling",
    [
        (11, 5, stirling2nd(11, 5)),
        (10, 5, stirling2nd(10, 5)),
        (11, 6, stirling2nd(11, 6)),
        (10, 6, stirling2nd(10, 6)),
    ],
)
def test_set_partition(n: int, k: int, expected_stirling: int) -> None:
    cnt = 1
    for _ in set_partition(n, k):
        cnt += 1
    assert cnt == expected_stirling


def test_set_partition_special() -> None:
    cnt = 1
    for _ in set_partition(6, 6):
        cnt += 1
    assert cnt == 1
    for _ in set_partition(5, 5):
        cnt += 1
    assert cnt == 1


@pytest.mark.parametrize(
    "n, expected_stirling",
    [
        (11, stirling2nd2(11)),
        (10, stirling2nd2(10)),
        (2, stirling2nd2(2)),
    ],
)
def test_set_bipart(n: int, expected_stirling: int) -> None:
    cnt = 1
    for _ in set_bipart(n):
        cnt += 1
    assert cnt == expected_stirling
