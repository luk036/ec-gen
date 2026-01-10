# Rust AI - Enumerative Combinatoric Generation

A Rust port of the Python `ec-gen` library for generating combinatorial objects.

## Overview

This library provides Rust implementations of algorithms for generating:
- Combinations (using EMK algorithm)
- Gray codes (Binary Reflected Gray Code)
- Permutations (Steinhaus-Johnson-Trotter and EHR algorithms)
- Set partitions and bipartitions
- Stirling numbers of the second kind

## Modules

- `combin`: Combinations generation
- `gray_code`: Binary reflected Gray code generation
- `sjt`: Steinhaus-Johnson-Trotter permutation algorithm
- `ehr`: Ehrlich-Hopcroft-Reingold permutation algorithm
- `set_partition`: Set partition generation
- `set_bipart`: Set bipartition generation
- `skeleton`: Example functions (Fibonacci)

## Usage

Add to your `Cargo.toml`:

```toml
[dependencies]
rust_ai = { path = "./rust_ai" }
```

Example:

```rust
use rust_ai::combin::comb;
use rust_ai::gray_code::brgc;

// Calculate combinations
let c = comb(6, 3); // 20

// Generate Gray codes
for code in brgc(3) {
    println!("{:?}", code);
}
```

## Status

This is a work-in-progress conversion from Python to Rust. Some algorithms are fully implemented while others are simplified placeholders.

## Building

```bash
cd rust_ai
cargo build
cargo test
```

## License

MIT
