#pragma once

#include <cppcoro/generator.hpp>
#include <cstdint>
#include <vector>
#include <concepts>
#include <ranges>

namespace ecgen {

    /**
     * @brief Generate all set bipartitions (partitions into 2 blocks)
     *
     * Generates all ways to partition a set of n elements into 2 blocks.
     *
     * @param n Size of the set
     * @return Generator yielding bipartitions as pairs of vectors
     */
    auto set_bipart_gen(int n) -> cppcoro::generator<std::pair<std::vector<int>, std::vector<int>>>;

    /**
     * @brief Generate set bipartitions with specified block sizes
     *
     * Generates all bipartitions where the first block has size k.
     *
     * @param n Total size of set
     * @param k Size of first block
     * @return Generator yielding bipartitions
     */
    auto set_bipart_k_gen(int n, int k) -> cppcoro::generator<std::pair<std::vector<int>, std::vector<int>>>;

    /**
     * @brief Number of bipartitions
     *
     * @param n Size of set
     * @return Number of ways to partition into 2 blocks (2^n - 2)
     */
    constexpr auto set_bipart_count(int n) -> std::size_t {
        if (n <= 1) return 0;
        return (1ULL << n) - 2;
    }

    /**
     * @brief Number of bipartitions with first block size k
     *
     * @param n Total size
     * @param k First block size
     * @return Number of such bipartitions (C(n,k))
     */
    template<std::integral T>
    constexpr auto set_bipart_k_count(T n, T k) -> std::size_t {
        if (k <= 0 || k >= n) return 0;
        return comb(n, k);
    }

} // namespace ecgen
