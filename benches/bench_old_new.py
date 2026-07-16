import gc
import time

from ec_gen.combin import comb, emk_comb_gen
from ec_gen.combin_old import emk_gen
from ec_gen.set_partition import set_partition, stirling2nd
from ec_gen.set_partition_old import set_partition as set_partition_old


def bench(name, fn, expected=None):
    gc.collect()
    start = time.perf_counter()
    cnt = fn()
    elapsed = (time.perf_counter() - start) * 1000
    print(f"  {name:<25} {cnt:>8}  {elapsed:>10.3f} ms")
    if expected is not None and cnt != expected:
        print(f"    WARNING: expected {expected}, got {cnt}")


print("=== Python: Old vs New ===")

# EMK with n=16,k=5 (same as C++ BM_EMK new)
print(f"\nEMK combinations n=16, k=5  (C(16,5)={comb(16, 5)})")
bench("new (4-helper)", lambda: sum(1 for _ in emk_comb_gen(16, 5)) + 1, comb(16, 5))
bench("old (2-helper)", lambda: sum(1 for _ in emk_gen(16, 5)) + 1, comb(16, 5))

# EMK with n=18,k=7 (same as pytest benchmark)
print(f"\nEMK combinations n=18, k=7  (C(18,7)={comb(18, 7)})")
bench("new (4-helper)", lambda: sum(1 for _ in emk_comb_gen(18, 7)) + 1, comb(18, 7))
bench("old (2-helper)", lambda: sum(1 for _ in emk_gen(18, 7)) + 1, comb(18, 7))

# Set partition
s = stirling2nd(11, 5)
print(f"\nSet partition n=11,k=5  (S(11,5)={s})")
bench("new (8-function)", lambda: sum(1 for _ in set_partition(11, 5)) + 1, s)
bench("old (8-function)", lambda: sum(1 for _ in set_partition_old(11, 5)) + 1, s)

s2 = stirling2nd(14, 3)
print(f"\nSet partition n=14,k=3  (S(14,3)={s2})")
bench("new (8-function)", lambda: sum(1 for _ in set_partition(14, 3)) + 1, s2)
bench("old (8-function)", lambda: sum(1 for _ in set_partition_old(14, 3)) + 1, s2)
