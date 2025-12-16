#include "ecgen/gray_code.hpp"
#include <algorithm>
#include <bit>

namespace ecgen {

    auto gray_code_gen(int n) -> cppcoro::generator<std::uint64_t> {
        if (n <= 0) {
            co_return;
        }
        
        std::uint64_t total = 1ULL << n;
        for (std::uint64_t i = 0; i < total; ++i) {
            co_yield binary_to_gray(i);
        }
    }

    auto gray_code_combinations(int n, int k) -> cppcoro::generator<std::uint64_t> {
        if (k <= 0 || k > n) {
            co_return;
        }
        
        // Start with first combination: lowest k bits set
        std::uint64_t comb = (1ULL << k) - 1;
        std::uint64_t limit = 1ULL << n;
        
        while (comb < limit) {
            co_yield comb;
            
            // Compute next combination using Gosper's hack
            std::uint64_t x = comb & -comb;
            std::uint64_t y = comb + x;
            comb = (((comb & ~y) / x) >> 1) | y;
        }
    }

} // namespace ecgen