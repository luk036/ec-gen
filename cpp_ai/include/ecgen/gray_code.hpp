#pragma once

#include <cppcoro/generator.hpp>
#include <cstdint>
#include <vector>
#include <bit>
#include <concepts>
#include <ranges>

namespace ecgen {

    /**
     * @brief Generate binary reflected Gray code
     * 
     * Generates Gray code sequence of length n bits.
     * Each successive code differs from the previous by exactly one bit.
     * 
     * @param n Number of bits
     * @return Generator yielding Gray codes as integers
     */
    auto gray_code_gen(int n) -> cppcoro::generator<std::uint64_t>;

    /**
     * @brief Convert binary to Gray code
     * 
     * @param binary Binary number
     * @return Gray code equivalent
     */
    template<std::unsigned_integral T>
    constexpr auto binary_to_gray(T binary) -> T {
        return binary ^ (binary >> 1);
    }

    /**
     * @brief Convert Gray code to binary
     * 
     * @param gray Gray code number
     * @return Binary equivalent
     */
    template<std::unsigned_integral T>
    constexpr auto gray_to_binary(T gray) -> T {
        T binary = gray;
        while (gray >>= 1) {
            binary ^= gray;
        }
        return binary;
    }

    /**
     * @brief Generate all subsets using Gray code
     * 
     * Generates all subsets of a set using Gray code ordering.
     * Each subset differs from the previous by exactly one element.
     * 
     * @tparam Container Type of container
     * @param container The set
     * @return Generator yielding subsets as vectors of elements
     */
    template<typename Container>
    auto gray_code_subsets(const Container& container) -> cppcoro::generator<std::vector<typename Container::value_type>> {
        int n = std::size(container);
        std::vector<typename Container::value_type> current;
        
        co_yield current; // Empty set
        
        for (std::uint64_t gray = 1; gray < (1ULL << n); ++gray) {
            // Find which bit changed
            std::uint64_t changed = gray ^ (gray - 1);
            int bit_pos = std::countr_zero(changed);
            
            if (gray & changed) {
                // Bit set: add element
                current.push_back(container[bit_pos]);
            } else {
                // Bit cleared: remove element
                auto it = std::find(current.begin(), current.end(), container[bit_pos]);
                if (it != current.end()) {
                    current.erase(it);
                }
            }
            
            co_yield current;
        }
    }

    /**
     * @brief Generate all combinations using Gray code
     * 
     * Generates all k-combinations of n elements using Gray code.
     * 
     * @param n Total number of elements
     * @param k Size of combinations
     * @return Generator yielding combinations as bitmasks
     */
    auto gray_code_combinations(int n, int k) -> cppcoro::generator<std::uint64_t>;

} // namespace ecgen