from ec_gen.set_bipart import set_bipart, stirling2nd2
from ec_gen.set_partition import set_partition, stirling2nd


def test_set_partition_odd_odd():
    cnt = 1
    for _ in set_partition(7, 3):
        cnt += 1
    assert cnt == stirling2nd(7, 3)


def test_set_partition_even_odd():
    cnt = 1
    for _ in set_partition(6, 3):
        cnt += 1
    assert cnt == stirling2nd(6, 3)


def test_set_partition_odd_even():
    cnt = 1
    for _ in set_partition(7, 4):
        cnt += 1
    assert cnt == stirling2nd(7, 4)


def test_set_partition_even_even():
    cnt = 1
    for _ in set_partition(6, 4):
        cnt += 1
    assert cnt == stirling2nd(6, 4)


def test_set_bipart_odd():
    cnt = 1
    for _ in set_bipart(7):
        cnt += 1
    assert cnt == stirling2nd2(7)


def test_set_bipart_even():
    cnt = 1
    for _ in set_bipart(6):
        cnt += 1
    assert cnt == stirling2nd2(6)
