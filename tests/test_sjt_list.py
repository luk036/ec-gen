
from ec_gen.sjt_list import sjt2

def test_sjt2():
    p = list(sjt2(3))
    assert p == [[0, 1, 2], [0, 2, 1], [2, 0, 1], [2, 1, 0], [1, 2, 0], [1, 0, 2]]
