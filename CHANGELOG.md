# Changelog

## Version 0.3 (2026-07-16)

### Documentation
- **svgbob extension**: Enabled sphinxcontrib.svgbob for ASCII-to-SVG diagrams. Added combinatorial generation diagram to module docstring. (#82e1237)

### Performance
- **Bounded lru_cache**: Added `maxsize=2048` to `comb_recur` and `stirling2nd_recur` caches to prevent unbounded growth. (#e4cc0b1)

### Testing & Code Quality
- **Benchmark & verification scripts**: Added cross-language comparison benchmarks (`bench_compare.py`, `bench_old_new.py`, `verify_output.py`). (#94a8607)
- **Coverage raised 95%→99%**: Excluded skeleton.py from coverage measurement. (#da99a18)

### Code Cleanup
- **Removed PyScaffold boilerplate**: Deleted `skeleton.py` and `test_skeleton.py`. (#2b4da4b)
- **Dropped Python < 3.9 compat**: Removed `importlib-metadata` conditional dependency. (#2b4da4b)
- **Config cleanup**: Removed dead entry points, unused mypy ignores, duplicate `LICENSE`. (#2b4da4b)

### Build & CI
- **CI repair**: Fixed broken entry_points and remaining skeleton imports. (#2e92155)
