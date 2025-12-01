# -*- coding: utf-8 -*-
from __future__ import print_function

import ec_gen.set_partition_old as old
from ec_gen.set_partition import set_partition, stirling2nd


def run_set_partition_new(n, k):
    cnt = 1
    for _ in set_partition(n, k):
        cnt += 1
    return cnt


def run_set_partition_old(n, k):
    cnt = 1
    for _ in old.set_partition(n, k):
        cnt += 1
    return cnt


def test_set_partition_new(benchmark) -> None:
    """[summary]

    Arguments:
        benchmark ([type]): [description]
    """
    n = 11
    k = 5
    cnt = benchmark(run_set_partition_new, n, k)
    assert cnt == stirling2nd(n, k)


def test_set_partition_old(benchmark) -> None:
    """[summary]

    Arguments:
        benchmark ([type]): [description]
    """
    n = 11
    k = 5
    cnt = benchmark(run_set_partition_old, n, k)
    assert cnt == stirling2nd(n, k)
