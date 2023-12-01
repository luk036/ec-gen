# -*- coding: utf-8 -*-
from __future__ import print_function

from ec_gen.combin import EMK_comb_gen, comb
from ec_gen.combin_old import EMK_gen


def run_EMK_new(n, k):
    cnt = 1
    for _ in EMK_comb_gen(n, k):
        cnt += 1
    return cnt


def run_EMK_old(n, k):
    cnt = 1
    for _ in EMK_gen(n, k):
        cnt += 1
    return cnt


def test_EMK_new(benchmark):
    """[summary]

    Arguments:
        benchmark ([type]): [description]
    """
    n = 16
    k = 5
    cnt = benchmark(run_EMK_new, 16, 5)
    assert cnt == comb(n, k)


def test_EMK_old(benchmark):
    """[summary]

    Arguments:
        benchmark ([type]): [description]
    """
    n = 16
    k = 5
    cnt = benchmark(run_EMK_old, 16, 5)
    assert cnt == comb(n, k)
