#include "ecgen/set_bipart.hpp"
#include <algorithm>
#include <bit>

namespace ecgen {

    auto set_bipart_gen(int n) -> cppcoro::generator<std::pair<std::vector<int>, std::vector<int>>> {
        if (n <= 1) {
            co_return;
        }
        
        // Generate all non-empty proper subsets
        std::uint64_t total_subsets = 1ULL << n;
        
        for (std::uint64_t mask = 1; mask < total_subsets - 1; ++mask) {
            std::vector<int> block1, block2;
            
            for (int i = 0; i < n; ++i) {
                if (mask & (1ULL << i)) {
                    block1.push_back(i + 1); // 1-based indexing
                } else {
                    block2.push_back(i + 1);
                }
            }
            
            co_yield {block1, block2};
        }
    }

    auto set_bipart_k_gen(int n, int k) -> cppcoro::generator<std::pair<std::vector<int>, std::vector<int>>> {
        if (k <= 0 || k >= n) {
            co_return;
        }
        
        // Start with first combination: lowest k bits set
        std::uint64_t comb = (1ULL << k) - 1;
        std::uint64_t limit = 1ULL << n;
        
        while (comb < limit) {
            std::vector<int> block1, block2;
            
            for (int i = 0; i < n; ++i) {
                if (comb & (1ULL << i)) {
                    block1.push_back(i + 1);
                } else {
                    block2.push_back(i + 1);
                }
            }
            
            co_yield {block1, block2};
            
            // Compute next combination using Gosper's hack
            std::uint64_t x = comb & -comb;
            std::uint64_t y = comb + x;
            comb = (((comb & ~y) / x) >> 1) | y;
        }
    }

} // namespace ecgen