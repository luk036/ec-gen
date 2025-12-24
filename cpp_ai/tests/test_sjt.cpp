#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "doctest.h"
#include "ecgen/sjt.hpp"
#include <vector>
#include <algorithm>
#include <set>

TEST_CASE("SJT permutation generation") {
    SUBCASE("Permutations of 3 elements") {
        std::vector<int> items = {1, 2, 3};
        std::vector<std::vector<int>> permutations;
        
        for (auto& perm : ecgen::sjt_apply(3, items)) {
            permutations.push_back(items);
        }
        
        // Should generate 3! = 6 permutations
        CHECK(permutations.size() == 6);
        
        // Check that all permutations are unique
        std::set<std::vector<int>> unique_permutations(
            permutations.begin(), permutations.end()
        );
        CHECK(unique_permutations.size() == 6);
        
        // Check that each permutation differs from previous by one adjacent swap
        for (size_t idx = 1; idx < permutations.size(); ++idx) {
            const auto& prev = permutations[idx - 1];
            const auto& curr = permutations[idx];
            
            // Count differences
            int diff_count = 0;
            for (size_t pos = 0; pos < prev.size(); ++pos) {
                if (prev[pos] != curr[pos]) {
                    ++diff_count;
                }
            }
            
            // Should differ by exactly 2 elements (one swap)
            CHECK(diff_count == 2);
            
            // The differing elements should be adjacent in one of the permutations
            bool adjacent_swap = false;
            for (size_t pos = 0; pos < prev.size() - 1; ++pos) {
                if ((prev[pos] == curr[pos + 1] && prev[pos + 1] == curr[pos]) &&
                    (prev[pos] != curr[pos] || prev[pos + 1] != curr[pos + 1])) {
                    adjacent_swap = true;
                    break;
                }
            }
            CHECK(adjacent_swap);
        }
    }
    
    SUBCASE("Permutations of 4 elements") {
        std::vector<int> items = {1, 2, 3, 4};
        int count = 0;
        
        for (auto& perm : ecgen::sjt_apply(4, items)) {
            ++count;
        }
        
        CHECK(count == 24); // 4! = 24
    }
}

TEST_CASE("Plain changes algorithm") {
    SUBCASE("Compare with SJT for n=3") {
        std::vector<int> items_sjt = {1, 2, 3};
        std::vector<int> items_pc = {1, 2, 3};
        
        std::vector<std::vector<int>> perms_sjt, perms_pc;
        
        // Generate with SJT
        for (auto& perm : ecgen::sjt_apply(3, items_sjt)) {
            perms_sjt.push_back(items_sjt);
        }
        
        // Generate with Plain Changes
        for (auto& perm : ecgen::sjt_apply(3, items_pc)) {
            perms_pc.push_back(items_pc);
        }
        
        // Both should generate the same number of permutations
        CHECK(perms_sjt.size() == perms_pc.size());
        CHECK(perms_sjt.size() == 6);
        
        // The sets of permutations should be identical
        std::set<std::vector<int>> set_sjt(perms_sjt.begin(), perms_sjt.end());
        std::set<std::vector<int>> set_pc(perms_pc.begin(), perms_pc.end());
        CHECK(set_sjt == set_pc);
    }
}

TEST_CASE("Factorial calculation") {
    SUBCASE("Small factorials") {
        CHECK(ecgen::factorial(0) == 1);
        CHECK(ecgen::factorial(1) == 1);
        CHECK(ecgen::factorial(2) == 2);
        CHECK(ecgen::factorial(3) == 6);
        CHECK(ecgen::factorial(4) == 24);
        CHECK(ecgen::factorial(5) == 120);
    }
}