from ec_gen.set_bipart import set_bipart, stirling2nd2
from ec_gen.set_partition import set_partition, stirling2nd


def test_set_partition():
    cnt = 1
    for _ in set_partition(5, 3):
        cnt += 1
    assert cnt == stirling2nd(5, 3)


def test_set_bipart_odd():
    cnt = 1
    for _ in set_bipart(5):
        cnt += 1
    assert cnt == stirling2nd2(5)


def test_set_bipart_even():
    cnt = 1
    for _ in set_bipart(6):
        cnt += 1
    assert cnt == stirling2nd2(6)
