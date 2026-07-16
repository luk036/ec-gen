import time
import gc
from ec_gen.combin import emk_comb_gen, comb
from ec_gen.sjt import sjt_gen
from ec_gen.ehr import ehr_gen
from ec_gen.gray_code import brgc_gen
from ec_gen.set_partition import set_partition, stirling2nd
from ec_gen.set_bipart import set_bipart, stirling2nd2

def bench(name, fn, expected=None):
    gc.collect()
    start = time.perf_counter()
    cnt = fn()
    elapsed = (time.perf_counter() - start) * 1000
    print(f"{name:<30} {cnt:>10}  {elapsed:>8.3f} ms")
    if expected is not None and cnt != expected:
        print(f"  WARNING: expected {expected}, got {cnt}")

print(f"{'Operation':<30} {'Count':>10}  {'Time':>10}")
print("-" * 55)

bench("emk_comb_gen(16,5)", lambda: sum(1 for _ in emk_comb_gen(16, 5)) + 1, comb(16, 5))
bench("emk_comb_gen(10,5)", lambda: sum(1 for _ in emk_comb_gen(10, 5)) + 1, comb(10, 5))
bench("sjt_gen(8)", lambda: sum(1 for _ in sjt_gen(8)), 40320)
bench("sjt_gen(7)", lambda: sum(1 for _ in sjt_gen(7)), 5040)
bench("sjt_gen(5)", lambda: sum(1 for _ in sjt_gen(5)), 120)
bench("ehr_gen(8)", lambda: sum(1 for _ in ehr_gen(8)) + 1, 40320)
bench("brgc_gen(12)", lambda: sum(1 for _ in brgc_gen(12)), 4095)
bench("brgc_gen(8)", lambda: sum(1 for _ in brgc_gen(8)), 255)
bench("set_partition(11,5)", lambda: sum(1 for _ in set_partition(11, 5)) + 1, stirling2nd(11, 5))
bench("set_partition(8,4)", lambda: sum(1 for _ in set_partition(8, 4)) + 1, stirling2nd(8, 4))
bench("set_bipart(15)", lambda: sum(1 for _ in set_bipart(15)) + 1, stirling2nd2(15))
bench("set_bipart(10)", lambda: sum(1 for _ in set_bipart(10)) + 1, stirling2nd2(10))
