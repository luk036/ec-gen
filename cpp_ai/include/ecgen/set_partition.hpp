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
    constexpr auto stirling2nd(T n, U k) -> std::size_t {
        if (k == 0 || k > n) return 0;
        if (k == 1 || k == n) return 1;
        
        // Use dynamic programming for runtime computation
        std::vector<std::size_t> prev(k + 1, 0), curr(k + 1, 0);
        prev[1] = 1;
        
        for (T i = 2; i <= n; ++i) {
            curr[1] = 1;
            for (U j = 2; j <= k && j <= i; ++j) {
                curr[j] = j * prev[j] + prev[j - 1];
            }
            std::swap(prev, curr);
        }
        
        return prev[k];
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
    constexpr auto bell(T n) -> std::size_t {
        if (n == 0) return 1;
        
        std::vector<std::size_t> bell_numbers(n + 1, 0);
        bell_numbers[0] = 1;
        
        for (T i = 1; i <= n; ++i) {
            bell_numbers[i] = 0;
            for (T k = 0; k < i; ++k) {
                bell_numbers[i] += comb(i - 1, k) * bell_numbers[k];
            }
        }
        
        return bell_numbers[n];
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
    constexpr auto comb(T n, T k) -> std::size_t {
        if (k > n) return 0;
        if (k == 0 || k == n) return 1;
        
        std::size_t result = 1;
        k = std::min(k, n - k);
        
        for (T i = 1; i <= k; ++i) {
            result = result * (n - k + i) / i;
        }
        
        return result;
    }

} // namespace ecgen