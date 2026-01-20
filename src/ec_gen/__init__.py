import sys

if sys.version_info[:2] >= (3, 8):
    # TODO: Import directly (no need for conditional) when `python_requires = >= 3.9`
    from importlib.metadata import PackageNotFoundError, version  # pragma: no cover
else:
    from importlib_metadata import PackageNotFoundError, version  # pragma: no cover

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = "ec-gen"
    __version__ = version(dist_name)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError

# Combinations
from ec_gen.combin import comb, emk, emk_comb_gen

# Gray codes
from ec_gen.gray_code import brgc, brgc_gen

# Permutations
from ec_gen.sjt import PlainChanges, sjt_gen

# Permutations (list form)
from ec_gen.sjt_list import sjt2

# Set partitions
from ec_gen.set_partition import set_partition, stirling2nd

# Set bipartitions
from ec_gen.set_bipart import set_bipart, stirling2nd2

# EHR permutations
from ec_gen.ehr import ehr_gen

__all__ = [
    # Combinations
    "comb",
    "emk",
    "emk_comb_gen",
    # Gray codes
    "brgc",
    "brgc_gen",
    # Permutations
    "PlainChanges",
    "sjt_gen",
    "sjt2",
    # Set partitions
    "set_partition",
    "stirling2nd",
    # Set bipartitions
    "set_bipart",
    "stirling2nd2",
    # EHR permutations
    "ehr_gen",
]
