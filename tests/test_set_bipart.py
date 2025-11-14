from ec_gen.set_bipart import set_bipart, stirling2nd2


def test_stirling2nd2():
    assert stirling2nd2(3) == 3
    assert stirling2nd2(4) == 7
    assert stirling2nd2(5) == 15
    assert stirling2nd2(6) == 31


def test_set_bipart_3():
    s = list(set_bipart(3))
    assert s == [2, 3]


def test_set_bipart_4():
    s = list(set_bipart(4))
    assert s == [3, 2, 3, 4, 3, 2]
