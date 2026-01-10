#include "ecgen/combin.hpp"
#include <algorithm>
#include <stack>
#include <tuple>

namespace ecgen {

    // Forward declarations
    static auto emk_comb_gen_odd(int n, int k) -> cppcoro::recursive_generator<std::pair<int, int>>;

    // Helper function for EMK combination generation
    static auto emk_comb_gen_even(int num, int select) -> cppcoro::recursive_generator<std::pair<int, int>> {
        if (select % 2 == 0) {
            if (select == 0) {
                co_return;
            }

            // Even select case
            for (const auto& [first, second] : emk_comb_gen_even(num - 1, select - 1)) {
                co_yield {first, second};
            }
            co_yield {select - 1, num - 1};

            for (const auto& [first, second] : emk_comb_gen_odd(num - 2, select - 2)) {
                co_yield {first, second};
            }
            co_yield {0, select - 2};

            for (const auto& [first, second] : emk_comb_gen_even(num - 2, select - 2)) {
                co_yield {first + 1, second + 1};
            }
            co_yield {select - 2, num - 2};

            for (const auto& [first, second] : emk_comb_gen_odd(num - 2, select)) {
                co_yield {first + 1, second + 1};
            }
        }
    }

    static auto emk_comb_gen_odd(int num, int select) -> cppcoro::recursive_generator<std::pair<int, int>> {
        if (select % 2 == 1) {
            if (select == 1) {
                for (int idx = 0; idx < num - 1; ++idx) {
                    co_yield {0, idx + 1};
                }
                co_return;
            }

            // Odd select case
            for (const auto& [first, second] : emk_comb_gen_odd(num - 1, select - 1)) {
                co_yield {first, second};
            }
            co_yield {select - 1, num - 1};

            for (const auto& [first, second] : emk_comb_gen_even(num - 2, select - 2)) {
                co_yield {first, second};
            }
            co_yield {0, select - 2};

            for (const auto& [first, second] : emk_comb_gen_odd(num - 2, select - 2)) {
                co_yield {first + 1, second + 1};
            }
            co_yield {select - 2, num - 2};

            for (const auto& [first, second] : emk_comb_gen_even(num - 2, select)) {
                co_yield {first + 1, second + 1};
            }
        }
    }

    auto emk_comb_gen(int num, int select) -> cppcoro::recursive_generator<std::pair<int, int>> {
        if (select <= 0 || select >= num) {
            co_return;
        }

        if (select % 2 == 0) {
            for (const auto& [first, second] : emk_comb_gen_even(num, select)) {
                co_yield {first, second};
            }
        } else {
            for (const auto& [first, second] : emk_comb_gen_odd(num, select)) {
                co_yield {first, second};
            }
        }
    }

} // namespace ecgen
