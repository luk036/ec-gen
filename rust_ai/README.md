# Rust AI - Combinatorial Generation Algorithms

Rust implementation of combinatorial generation algorithms using `genawaiter` for async/await-style generators.

This is a Rust port of the Python `ec-gen` library, providing efficient combinatorial generation algorithms.

## Algorithms Implemented

1. **Combinations Generator** (`combin.rs`) - EMK algorithm for generating combinations
2. **Ehrlich-Hopcroft-Reingold Algorithm** (`ehr.rs`) - Permutation generation
3. **Binary Reflected Gray Code** (`gray_code.rs`) - Gray code generation
4. **Set Bipartition** (`set_bipart.rs`) - Set bipartition generation
5. **Set Partition** (`set_partition.rs`) - Set partition generation
6. **Steinhaus-Johnson-Trotter Algorithm** (`sjt.rs`) - Permutation generation
7. **Skeleton** (`skeleton.rs`) - Example and utility functions

## Usage

Add to your `Cargo.toml`:

```toml
[dependencies]
rust_ai = { git = "https://github.com/luk036/ec-gen" }
```

Example usage:

```rust
use rust_ai::combin::emk;

fn main() {
    for combination in emk(6, 3, 0, 1) {
        println!("{:?}", combination);
    }
}
```

## Features

- **Async/await style generators** using `genawaiter`
- **Zero-cost abstractions** - Rust's performance advantages
- **Memory efficient** - Generates sequences lazily
- **Type safe** - Compile-time guarantees
- **Thread safe** - Can be used in concurrent contexts

## Benchmarks

Run benchmarks with:

```bash
cargo bench
```

## License

MIT License - see LICENSE file for details.