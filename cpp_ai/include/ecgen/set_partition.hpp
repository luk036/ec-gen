#pragma once

#include <cppcoro/generator.hpp>
#include <cstdint>
#include <vector>
#include <array>
#include <concepts>
#include <ranges>

namespace ecgen {

    /**
     * @brief Stirling numbers of the second kind S(n,k)
     *
     * Computes the number of ways to partition a set of n labeled objects
     * into k non-empty unlabeled subsets.
     *
     * @tparam N Set size
     * @tparam K Number of non-empty subsets
     * @return constexpr std::size_t Stirling number S(N,K)
     */
    template<std::integral T, std::integral U>
    constexpr auto stirling2nd(T num, U select) -> std::size_t {
        if (select == 0 || select > num) return 0;
        if (select == 1 || select == num) return 1;

        // Use dynamic programming for runtime computation
        std::vector<std::size_t> prev(select + 1, 0), curr(select + 1, 0);
        prev[1] = 1;

        for (T idx = 2; idx <= num; ++idx) {
            curr[1] = 1;
            for (U pos = 2; pos <= select && pos <= idx; ++pos) {
                curr[pos] = pos * prev[pos] + prev[pos - 1];
            }
            std::swap(prev, curr);
        }

        return prev[select];
    }

    /**
     * @brief Bell numbers B(n)
     *
     * Computes the number of partitions of a set of n labeled elements.
     *
     * @tparam N Set size
     * @return constexpr std::size_t Bell number B(N)
     */
    template<std::integral T>
    constexpr auto bell(T num) -> std::size_t {
        if (num == 0) return 1;

        std::vector<std::size_t> bell_numbers(num + 1, 0);
        bell_numbers[0] = 1;

        for (T idx = 1; idx <= num; ++idx) {
            bell_numbers[idx] = 0;
            for (T select = 0; select < idx; ++select) {
                bell_numbers[idx] += comb(idx - 1, select) * bell_numbers[select];
            }
        }

        return bell_numbers[num];
    }

    /**
     * @brief Generate all set partitions using restricted growth strings
     *
     * Generates all partitions of the set {1,2,...,n} using the
     * restricted growth string representation.
     *
     * @param n Size of the set
     * @return Generator yielding partitions as vectors of block indices
     */
    auto set_partition_gen(int n) -> cppcoro::generator<std::vector<int>>;

    /**
     * @brief Generate set partitions with exactly k blocks
     *
     * @param n Size of the set
     * @param k Number of blocks
     * @return Generator yielding partitions as vectors of block indices
     */
    auto set_partition_k_gen(int n, int k) -> cppcoro::generator<std::vector<int>>;

    /**
     * @brief Helper function for combination calculation
     */
    template<std::integral T>
    constexpr auto comb(T num, T select) -> std::size_t {
        if (select > num) return 0;
        if (select == 0 || select == num) return 1;

        std::size_t result = 1;
        select = std::min(select, num - select);

        for (T idx = 1; idx <= select; ++idx) {
            result = result * (num - select + idx) / idx;
        }

        return result;
    }

} // namespace ecgen
