# -*- coding: utf-8 -*-
from __future__ import print_function

from ec_gen.combin import comb, emk_comb_gen
from ec_gen.combin_old import emk_gen


def run_emk_new(n, k):
    cnt = 1
    for _ in emk_comb_gen(n, k):
        cnt += 1
    return cnt


def run_emk_old(n, k):
    cnt = 1
    for _ in emk_gen(n, k):
        cnt += 1
    return cnt


def test_emk_new(benchmark) -> None:
    """[summary]

    Arguments:
        benchmark ([type]): [description]
    """
    n = 18
    k = 7
    cnt = benchmark(run_emk_new, n, k)
    assert cnt == comb(n, k)


def test_emk_old(benchmark) -> None:
    """[summary]

    Arguments:
        benchmark ([type]): [description]
    """
    n = 18
    k = 7
    cnt = benchmark(run_emk_old, n, k)
    assert cnt == comb(n, k)
