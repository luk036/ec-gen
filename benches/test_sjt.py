# -*- coding: utf-8 -*-
from __future__ import print_function

from ec_gen.sjt import SJT_gen
from ec_gen.sjt_list import SJT2


def run_sjt_new(n):
    alphabets = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    cnt = 0
    for x in SJT_gen(n):
        cnt += 1
        alphabets[x], alphabets[x + 1] = alphabets[x + 1], alphabets[x]
    return cnt


def run_sjt_old(n):
    alphabets = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    cnt = 0
    for perm in SJT2(n):
        _ = list(alphabets[i] for i in perm)
        cnt += 1
    return cnt


def test_sjt_new(benchmark):
    """[summary]

    Arguments:
        benchmark ([type]): [description]
    """
    cnt = benchmark(run_sjt_new, 8)
    assert cnt == 40320


def test_sjt_old(benchmark):
    """[summary]

    Arguments:
        benchmark ([type]): [description]
    """
    cnt = benchmark(run_sjt_old, 8)
    assert cnt == 40320
