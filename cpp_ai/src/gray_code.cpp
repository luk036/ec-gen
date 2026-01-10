#include "ecgen/gray_code.hpp"
#include <algorithm>
#include <bit>

namespace ecgen {

    auto gray_code_gen(int num) -> cppcoro::generator<std::uint64_t> {
        if (num <= 0) {
            co_return;
        }

        std::uint64_t total = 1ULL << num;
        for (std::uint64_t idx = 0; idx < total; ++idx) {
            co_yield binary_to_gray(idx);
        }
    }

    auto gray_code_combinations(int num, int select) -> cppcoro::generator<std::uint64_t> {
        if (select <= 0 || select > num) {
            co_return;
        }

        // Start with first combination: lowest select bits set
        std::uint64_t comb = (1ULL << select) - 1;
        std::uint64_t limit = 1ULL << num;

        while (comb < limit) {
            co_yield comb;

            // Compute next combination using Gosper's hack
            std::uint64_t temp = comb & -comb;
            std::uint64_t next_val = comb + temp;
            comb = (((comb & ~next_val) / temp) >> 1) | next_val;
        }
    }

} // namespace ecgen
