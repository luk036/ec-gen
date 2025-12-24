#include "ecgen/set_bipart.hpp"
#include <algorithm>
#include <bit>

namespace ecgen {

    auto set_bipart_gen(int num) -> cppcoro::generator<std::pair<std::vector<int>, std::vector<int>>> {
        if (num <= 1) {
            co_return;
        }
        
        // Generate all non-empty proper subsets
        std::uint64_t total_subsets = 1ULL << num;
        
        for (std::uint64_t mask = 1; mask < total_subsets - 1; ++mask) {
            std::vector<int> block1, block2;
            
            for (int idx = 0; idx < num; ++idx) {
                if (mask & (1ULL << idx)) {
                    block1.push_back(idx + 1); // 1-based indexing
                } else {
                    block2.push_back(idx + 1);
                }
            }
            
            co_yield {block1, block2};
        }
    }

    auto set_bipart_k_gen(int num, int select) -> cppcoro::generator<std::pair<std::vector<int>, std::vector<int>>> {
        if (select <= 0 || select >= num) {
            co_return;
        }
        
        // Start with first combination: lowest select bits set
        std::uint64_t comb = (1ULL << select) - 1;
        std::uint64_t limit = 1ULL << num;
        
        while (comb < limit) {
            std::vector<int> block1, block2;
            
            for (int idx = 0; idx < num; ++idx) {
                if (comb & (1ULL << idx)) {
                    block1.push_back(idx + 1);
                } else {
                    block2.push_back(idx + 1);
                }
            }
            
            co_yield {block1, block2};
            
            // Compute next combination using Gosper's hack
            std::uint64_t temp = comb & -comb;
            std::uint64_t next_val = comb + temp;
            comb = (((comb & ~next_val) / temp) >> 1) | next_val;
        }
    }

} // namespace ecgen