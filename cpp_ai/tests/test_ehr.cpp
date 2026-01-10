#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "doctest.h"
#include "ecgen/ehr.hpp"
#include <vector>
#include <algorithm>
#include <set>

TEST_CASE("Ehrlich's algorithm") {
    SUBCASE("Permutations of 3 elements") {
        std::vector<std::vector<int>> permutations;

        for (auto perm : ecgen::ehr_gen(3)) {
            permutations.push_back(perm);
        }

        // Should generate 3! = 6 permutations
        CHECK(permutations.size() == 6);

        // Check that all permutations are unique
        std::set<std::vector<int>> unique_permutations(
            permutations.begin(), permutations.end()
        );
        CHECK(unique_permutations.size() == 6);

        // Verify each permutation contains all elements 1,2,3
        for (const auto& perm : permutations) {
            CHECK(perm.size() == 3);
            std::set<int> elements(perm.begin(), perm.end());
            CHECK(elements == std::set<int>{1, 2, 3});
        }
    }

    SUBCASE("Permutations of 4 elements") {
        int count = 0;

        for (auto perm : ecgen::ehr_gen(4)) {
            ++count;
            CHECK(perm.size() == 4);
        }

        CHECK(count == 24); // 4! = 24
    }
}

TEST_CASE("Ehrlich apply to container") {
    SUBCASE("Apply to vector of integers") {
        std::vector<int> items = {1, 2, 3};
        std::vector<std::vector<int>> permutations;

        for (auto& perm : ecgen::ehr_apply(items)) {
            permutations.push_back(items);
        }

        CHECK(permutations.size() == 6);

        // Check that original vector is restored
        CHECK(items == std::vector<int>{1, 2, 3});
    }

    SUBCASE("Apply to vector of strings") {
        std::vector<std::string> items = {"A", "B", "C"};
        int count = 0;

        for (auto& perm : ecgen::ehr_apply(items)) {
            ++count;
        }

        CHECK(count == 6);
        CHECK(items == std::vector<std::string>{"A", "B", "C"});
    }
}

TEST_CASE("Ehrlich count") {
    SUBCASE("Small permutation counts") {
        CHECK(ecgen::ehr_count(0) == 1);
        CHECK(ecgen::ehr_count(1) == 1);
        CHECK(ecgen::ehr_count(2) == 2);
        CHECK(ecgen::ehr_count(3) == 6);
        CHECK(ecgen::ehr_count(4) == 24);
        CHECK(ecgen::ehr_count(5) == 120);
    }

    SUBCASE("Compare with actual generation") {
        for (int n = 1; n <= 5; ++n) {
            int count = 0;
            for (auto perm : ecgen::ehr_gen(n)) {
                ++count;
            }
            CHECK(count == ecgen::ehr_count(n));
        }
    }
}
