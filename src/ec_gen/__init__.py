"""
ec_gen - Enumerative Combinatorics Generation

This package provides generators for various combinatorial structures including:

.. svgbob::
   :align: center

       {1,2,3} ──────► {1,2} {1,3} {2,3}
          │                │
          │                ▼
          │          ┌──────────┐
          └─────────►│ Permute  │
                     │  123     │
                     │  132     │
                     │  213     │
                     └──────────┘

- Combinations (via homogeneous revolving-door algorithm)
- Permutations (via Steinhaus-Johnson-Trotter and Ehrlich-Hopcroft-Reingold algorithms)
- Gray codes (binary reflected Gray code)
- Set partitions (via restricted growth strings)

Each module contains generator functions that yield successive elements of the
combinatorial structure, allowing memory-efficient iteration over large collections.

Example:
    >>> from ec_gen import comb, emk, brgc
    >>> comb(6, 3)  # Number of combinations
    20
    >>> for seq in emk(3, 1):
    ...     print(seq)
    [1, 0, 0]
    [0, 1, 0]
    [0, 0, 1]
"""

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

# EHR permutations
from ec_gen.ehr import ehr_gen

# Gray codes
from ec_gen.gray_code import brgc, brgc_gen

# Set bipartitions
from ec_gen.set_bipart import set_bipart, stirling2nd2

# Set partitions
from ec_gen.set_partition import set_partition, stirling2nd

# Permutations
from ec_gen.sjt import PlainChanges, sjt_gen

# Permutations (list form)
from ec_gen.sjt_list import sjt2

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
