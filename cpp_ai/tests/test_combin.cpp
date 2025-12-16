#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include "ecgen/combin.hpp"
#include <vector>
#include <algorithm>

TEST_CASE("Combination count") {
    SUBCASE("Basic combinations") {
        CHECK(ecgen::comb(6, 3) == 20);
        CHECK(ecgen::comb(6, 4) == ecgen::comb(6, 2));
        CHECK(ecgen::comb(6, 5) == ecgen::comb(6, 1));
        CHECK(ecgen::comb(6, 6) == ecgen::comb(6, 0));
    }
    
    SUBCASE("Edge cases") {
        CHECK(ecgen::comb(0, 0) == 1);
        CHECK(ecgen::comb(5, 0) == 1);
        CHECK(ecgen::comb(5, 5) == 1);
        CHECK(ecgen::comb(5, 6) == 0);
    }
}

TEST_CASE("EMK combination generation") {
    SUBCASE("4 choose 2") {
        std::vector<int> items = {1, 2, 3, 4};
        std::vector<std::vector<int>> combinations;
        
        for (auto& comb : ecgen::emk(4, 2, items)) {
            // Get the current combination (first 2 elements are selected)
            std::vector<int> current_comb(items.begin(), items.begin() + 2);
            combinations.push_back(current_comb);
        }
        
        // Should generate C(4,2) = 6 combinations
        CHECK(combinations.size() == 6);
        
        // Check that all combinations are unique
        std::sort(combinations.begin(), combinations.end());
        auto last = std::unique(combinations.begin(), combinations.end());
        CHECK(std::distance(combinations.begin(), last) == 6);
    }
    
    SUBCASE("3 choose 1") {
        std::vector<int> items = {1, 2, 3};
        std::vector<std::vector<int>> combinations;
        
        for (auto& comb : ecgen::emk(3, 1, items)) {
            std::vector<int> current_comb(items.begin(), items.begin() + 1);
            combinations.push_back(current_comb);
        }
        
        CHECK(combinations.size() == 3);
    }
}

TEST_CASE("Compile-time combination count") {
    SUBCASE("Basic compile-time combinations") {
        constexpr auto c42 = ecgen::Combination<4, 2>();
        CHECK(c42 == 6);
        
        constexpr auto c53 = ecgen::Combination<5, 3>();
        CHECK(c53 == 10);
        
        constexpr auto c66 = ecgen::Combination<6, 6>();
        CHECK(c66 == 1);
    }
}