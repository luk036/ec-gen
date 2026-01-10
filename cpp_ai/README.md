# ecgen-cpp: Enumerative Combinatoric Generation in C++23

A C++23 library for generating combinatorial objects, ported from the Python `ec-gen` project.

## Features

- **C++23 Modern Features**: Coroutines, concepts, ranges, and modules
- **Multiple Build Systems**: CMake and xmake support
- **Comprehensive Testing**: doctest-based test suite
- **Header-Only Dependencies**: Uses cppcoro for coroutine support
- **Python Parity**: Implements all algorithms from the Python `ec-gen` library

## Algorithms Implemented

### Combinations
- `emk()`: Generate k-combinations using revolving door algorithm
- `comb()`: Calculate binomial coefficients
- `Combination<N,K>()`: Compile-time combination count

### Permutations
- `sjt_gen()`: Steinhaus-Johnson-Trotter algorithm
- `plain_changes()`: Alternative SJT implementation
- `ehr_gen()`: Ehrlich's algorithm

### Set Partitions
- `set_partition_gen()`: Generate all set partitions
- `set_partition_k_gen()`: Partitions with exactly k blocks
- `stirling2nd()`: Stirling numbers of the second kind
- `bell()`: Bell numbers

### Gray Codes
- `gray_code_gen()`: Binary reflected Gray code
- `gray_code_subsets()`: Generate subsets using Gray code
- `gray_code_combinations()`: k-combinations via Gray code

### Set Bipartitions
- `set_bipart_gen()`: All bipartitions (partitions into 2 blocks)
- `set_bipart_k_gen()`: Bipartitions with specified block size

### Framework
- `skeleton.hpp`: Generic combinatorial generation framework

## Requirements

- C++23 compatible compiler (GCC 11+, Clang 14+, MSVC 19.29+)
- CMake 3.20+ or xmake
- Git (for downloading dependencies)

## Building with CMake

```bash
# Configure
cmake -B build -DCMAKE_BUILD_TYPE=Release

# Build
cmake --build build

# Run tests
cd build && ctest

# Install
cmake --install build --prefix /usr/local
```

## Building with xmake

```bash
# Configure and build
xmake

# Build tests
xmake config --tests=y
xmake build test_combin

# Run specific test
xmake run test_combin
```

## Usage Example

```cpp
#include <iostream>
#include <vector>
#include "ecgen/combin.hpp"

int main() {
    // Generate all 3-combinations of 5 elements
    std::vector<char> items = {'A', 'B', 'C', 'D', 'E'};

    for (auto& comb : ecgen::emk(5, 3, items)) {
        for (int i = 0; i < 3; ++i) {
            std::cout << items[i] << " ";
        }
        std::cout << "\n";
    }

    return 0;
}
```

## Project Structure

```
cpp_ai/
├── include/ecgen/          # Public headers
│   ├── combin.hpp          # Combinations
│   ├── set_partition.hpp   # Set partitions
│   ├── sjt.hpp            # SJT permutations
│   ├── gray_code.hpp      # Gray codes
│   ├── ehr.hpp           # Ehrlich permutations
│   ├── set_bipart.hpp    # Set bipartitions
│   ├── skeleton.hpp      # Generation framework
│   └── ecgen.hpp         # Main header
├── src/                   # Implementation
├── tests/                # doctest test files
├── examples/             # Example programs
├── CMakeLists.txt        # CMake build
└── xmake.lua            # xmake build
```

## Dependencies

- **cppcoro**: For coroutine support (bundled in `include/cppcoro/`)
- **doctest**: For testing (automatically downloaded)

## Testing

The library includes comprehensive tests for each module:

```bash
# Run all tests with CMake
cd build && ctest --output-on-failure

# Run specific test with xmake
xmake run test_sjt
```

## License

MIT License, same as the original Python project.

## Related Projects

- Python version: [ec-gen](https://github.com/luk036/ec-gen)
- Rust version: `rust_ai/` and `rust_ai_iterator/` in this repository

## Contributing

1. Follow the existing code style (C++23 with concepts and coroutines)
2. Add tests for new functionality
3. Update documentation
4. Ensure both CMake and xmake builds work

## Performance Notes

- Uses C++23 coroutines for lazy generation
- Compile-time computation where possible
- Minimal memory overhead for large combinatorial sets
- Iterator-based interfaces for integration with C++ ranges
