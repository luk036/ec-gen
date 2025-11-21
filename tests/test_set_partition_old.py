import pytest

from ec_gen.set_partition_old import set_partition, stirling2nd


@pytest.mark.parametrize(
    "n, k, expected_stirling",
    [
        (11, 5, stirling2nd(11, 5)),
        (10, 5, stirling2nd(10, 5)),
        (11, 6, stirling2nd(11, 6)),
        (10, 6, stirling2nd(10, 6)),
    ],
)
def test_set_partition(n, k, expected_stirling):
    cnt = 1
    for _ in set_partition(n, k):
        cnt += 1
    assert cnt == expected_stirling


def test_set_partition_special():
    cnt = 1
    for _ in set_partition(6, 6):
        cnt += 1
    assert cnt == 1
    for _ in set_partition(5, 5):
        cnt += 1
    assert cnt == 1
