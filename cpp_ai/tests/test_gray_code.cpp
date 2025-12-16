#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "doctest.h"
#include "ecgen/gray_code.hpp"
#include <vector>
#include <algorithm>
#include <set>
#include <bit>

TEST_CASE("Binary to Gray code conversion") {
    SUBCASE("Single bit conversions") {
        CHECK(ecgen::binary_to_gray(0b0) == 0b0);
        CHECK(ecgen::binary_to_gray(0b1) == 0b1);
    }
    
    SUBCASE("Multi-bit conversions") {
        CHECK(ecgen::binary_to_gray(0b00) == 0b00);
        CHECK(ecgen::binary_to_gray(0b01) == 0b01);
        CHECK(ecgen::binary_to_gray(0b10) == 0b11);
        CHECK(ecgen::binary_to_gray(0b11) == 0b10);
        
        CHECK(ecgen::binary_to_gray(0b000) == 0b000);
        CHECK(ecgen::binary_to_gray(0b001) == 0b001);
        CHECK(ecgen::binary_to_gray(0b010) == 0b011);
        CHECK(ecgen::binary_to_gray(0b011) == 0b010);
        CHECK(ecgen::binary_to_gray(0b100) == 0b110);
        CHECK(ecgen::binary_to_gray(0b101) == 0b111);
        CHECK(ecgen::binary_to_gray(0b110) == 0b101);
        CHECK(ecgen::binary_to_gray(0b111) == 0b100);
    }
}

TEST_CASE("Gray code to binary conversion") {
    SUBCASE("Round trip conversions") {
        for (uint64_t i = 0; i < 256; ++i) {
            uint64_t gray = ecgen::binary_to_gray(i);
            uint64_t binary = ecgen::gray_to_binary(gray);
            CHECK(binary == i);
        }
    }
    
    SUBCASE("Specific conversions") {
        CHECK(ecgen::gray_to_binary(0b00) == 0b00);
        CHECK(ecgen::gray_to_binary(0b01) == 0b01);
        CHECK(ecgen::gray_to_binary(0b11) == 0b10);
        CHECK(ecgen::gray_to_binary(0b10) == 0b11);
    }
}

TEST_CASE("Gray code generation") {
    SUBCASE("2-bit Gray code") {
        std::vector<uint64_t> codes;
        for (auto code : ecgen::gray_code_gen(2)) {
            codes.push_back(code);
        }
        
        CHECK(codes.size() == 4);
        
        // Check Gray code property: consecutive codes differ by exactly one bit
        for (size_t i = 1; i < codes.size(); ++i) {
            uint64_t diff = codes[i] ^ codes[i - 1];
            CHECK(std::popcount(diff) == 1);
        }
        
        // Check that all codes are unique
        std::set<uint64_t> unique_codes(codes.begin(), codes.end());
        CHECK(unique_codes.size() == 4);
    }
    
    SUBCASE("3-bit Gray code") {
        std::vector<uint64_t> codes;
        for (auto code : ecgen::gray_code_gen(3)) {
            codes.push_back(code);
        }
        
        CHECK(codes.size() == 8);
        
        // Check Gray code property
        for (size_t i = 1; i < codes.size(); ++i) {
            uint64_t diff = codes[i] ^ codes[i - 1];
            CHECK(std::popcount(diff) == 1);
        }
    }
}

TEST_CASE("Gray code subsets") {
    SUBCASE("Subsets of 3 elements") {
        std::vector<char> items = {'A', 'B', 'C'};
        std::vector<std::vector<char>> subsets;
        
        for (auto subset : ecgen::gray_code_subsets(items)) {
            subsets.push_back(subset);
        }
        
        CHECK(subsets.size() == 8); // 2^3 = 8 subsets
        
        // Check that consecutive subsets differ by exactly one element
        for (size_t i = 1; i < subsets.size(); ++i) {
            const auto& prev = subsets[i - 1];
            const auto& curr = subsets[i];
            
            // Find symmetric difference
            std::vector<char> diff;
            std::set_symmetric_difference(
                prev.begin(), prev.end(),
                curr.begin(), curr.end(),
                std::back_inserter(diff)
            );
            
            CHECK(diff.size() == 1);
        }
    }
}

TEST_CASE("Gray code combinations") {
    SUBCASE("4 choose 2 combinations") {
        std::vector<uint64_t> combinations;
        for (auto comb : ecgen::gray_code_combinations(4, 2)) {
            combinations.push_back(comb);
        }
        
        CHECK(combinations.size() == 6); // C(4,2) = 6
        
        // Check that each combination has exactly 2 bits set
        for (auto comb : combinations) {
            CHECK(std::popcount(comb) == 2);
        }
        
        // Check that combinations are unique
        std::set<uint64_t> unique_combs(combinations.begin(), combinations.end());
        CHECK(unique_combs.size() == 6);
        
        // Check revolving door property: consecutive combinations differ by
        // removing one element and adding another
        for (size_t i = 1; i < combinations.size(); ++i) {
            uint64_t diff = combinations[i] ^ combinations[i - 1];
            CHECK(std::popcount(diff) == 2);
        }
    }
}