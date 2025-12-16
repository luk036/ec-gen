#include "ecgen/combin.hpp"
#include <algorithm>
#include <stack>
#include <tuple>

namespace ecgen {

    // Forward declarations
    static auto emk_comb_gen_odd(int n, int k) -> cppcoro::recursive_generator<std::pair<int, int>>;
    
    // Helper function for EMK combination generation
    static auto emk_comb_gen_even(int n, int k) -> cppcoro::recursive_generator<std::pair<int, int>> {
        if (k % 2 == 0) {
            if (k == 0) {
                co_return;
            }
            
            // Even k case
            for (const auto& [x, y] : emk_comb_gen_even(n - 1, k - 1)) {
                co_yield {x, y};
            }
            co_yield {k - 1, n - 1};
            
            for (const auto& [x, y] : emk_comb_gen_odd(n - 2, k - 2)) {
                co_yield {x, y};
            }
            co_yield {0, k - 2};
            
            for (const auto& [x, y] : emk_comb_gen_even(n - 2, k - 2)) {
                co_yield {x + 1, y + 1};
            }
            co_yield {k - 2, n - 2};
            
            for (const auto& [x, y] : emk_comb_gen_odd(n - 2, k)) {
                co_yield {x + 1, y + 1};
            }
        }
    }

    static auto emk_comb_gen_odd(int n, int k) -> cppcoro::recursive_generator<std::pair<int, int>> {
        if (k % 2 == 1) {
            if (k == 1) {
                for (int i = 0; i < n - 1; ++i) {
                    co_yield {0, i + 1};
                }
                co_return;
            }
            
            // Odd k case
            for (const auto& [x, y] : emk_comb_gen_odd(n - 1, k - 1)) {
                co_yield {x, y};
            }
            co_yield {k - 1, n - 1};
            
            for (const auto& [x, y] : emk_comb_gen_even(n - 2, k - 2)) {
                co_yield {x, y};
            }
            co_yield {0, k - 2};
            
            for (const auto& [x, y] : emk_comb_gen_odd(n - 2, k - 2)) {
                co_yield {x + 1, y + 1};
            }
            co_yield {k - 2, n - 2};
            
            for (const auto& [x, y] : emk_comb_gen_even(n - 2, k)) {
                co_yield {x + 1, y + 1};
            }
        }
    }

    auto emk_comb_gen(int n, int k) -> cppcoro::recursive_generator<std::pair<int, int>> {
        if (k <= 0 || k >= n) {
            co_return;
        }
        
        if (k % 2 == 0) {
            for (const auto& [x, y] : emk_comb_gen_even(n, k)) {
                co_yield {x, y};
            }
        } else {
            for (const auto& [x, y] : emk_comb_gen_odd(n, k)) {
                co_yield {x, y};
            }
        }
    }

} // namespace ecgen