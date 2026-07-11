"""Verify output sequences match across languages by dumping small cases."""
from ec_gen.combin import emk_comb_gen
from ec_gen.sjt import sjt_gen
from ec_gen.ehr import ehr_gen
from ec_gen.gray_code import brgc_gen
from ec_gen.set_partition import set_partition
from ec_gen.set_bipart import set_bipart

def dump(name, seq):
    items = list(seq)
    print(f"{name} ({len(items)} items): {items}")
    return items

print("=== EMK combinations ===")
dump("emk_comb_gen(5,2)", emk_comb_gen(5, 2))
dump("emk_comb_gen(5,3)", emk_comb_gen(5, 3))

print("\n=== SJT permutations ===")
dump("sjt_gen(3)", sjt_gen(3))
dump("sjt_gen(4)", sjt_gen(4))

print("\n=== Ehrlich permutations ===")
dump("ehr_gen(3)", ehr_gen(3))
dump("ehr_gen(4)", ehr_gen(4))

print("\n=== BRGC ===")
dump("brgc_gen(3)", brgc_gen(3))

print("\n=== Set partition ===")
dump("set_partition(5,2)", set_partition(5, 2))

print("\n=== Set bipartition ===")
dump("set_bipart(5)", set_bipart(5))
