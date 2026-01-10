#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "doctest.h"
#include "ecgen/set_bipart.hpp"
#include <vector>
#include <algorithm>
#include <set>

TEST_CASE("Set bipartition count") {
    SUBCASE("Basic counts") {
        CHECK(ecgen::set_bipart_count(1) == 0);
        CHECK(ecgen::set_bipart_count(2) == 2);
        CHECK(ecgen::set_bipart_count(3) == 6);
        CHECK(ecgen::set_bipart_count(4) == 14);
    }

    SUBCASE("Count with specified block size") {
        CHECK(ecgen::set_bipart_k_count(4, 1) == 4);
        CHECK(ecgen::set_bipart_k_count(4, 2) == 6);
        CHECK(ecgen::set_bipart_count(4) == 14); // 4 + 6 + 4 = 14
    }
}

TEST_CASE("Set bipartition generation") {
    SUBCASE("Bipartitions of [3]") {
        std::vector<std::pair<std::vector<int>, std::vector<int>>> bipartitions;

        for (auto bipart : ecgen::set_bipart_gen(3)) {
            bipartitions.push_back(bipart);
        }

        // Should generate 2^3 - 2 = 6 bipartitions
        CHECK(bipartitions.size() == 6);

        // Check that each bipartition is valid
        for (const auto& [block1, block2] : bipartitions) {
            // Blocks should be non-empty
            CHECK(!block1.empty());
            CHECK(!block2.empty());

            // Blocks should be disjoint
            std::set<int> all_elements;
            all_elements.insert(block1.begin(), block1.end());
            all_elements.insert(block2.begin(), block2.end());
            CHECK(all_elements.size() == block1.size() + block2.size());

            // Union should be {1,2,3}
            CHECK(all_elements == std::set<int>{1, 2, 3});
        }

        // Check that all bipartitions are unique
        std::set<std::pair<std::set<int>, std::set<int>>> unique_biparts;
        for (const auto& [block1, block2] : bipartitions) {
            unique_biparts.insert({
                std::set<int>(block1.begin(), block1.end()),
                std::set<int>(block2.begin(), block2.end())
            });
        }
        CHECK(unique_biparts.size() == 6);
    }

    SUBCASE("Bipartitions of [4] with block size 2") {
        std::vector<std::pair<std::vector<int>, std::vector<int>>> bipartitions;

        for (auto bipart : ecgen::set_bipart_k_gen(4, 2)) {
            bipartitions.push_back(bipart);
        }

        // Should generate C(4,2) = 6 bipartitions
        CHECK(bipartitions.size() == 6);

        // Check that each bipartition has blocks of size 2
        for (const auto& [block1, block2] : bipartitions) {
            CHECK(block1.size() == 2);
            CHECK(block2.size() == 2);
        }
    }

    SUBCASE("Bipartitions of [5] with block size 1") {
        std::vector<std::pair<std::vector<int>, std::vector<int>>> bipartitions;

        for (auto bipart : ecgen::set_bipart_k_gen(5, 1)) {
            bipartitions.push_back(bipart);
        }

        // Should generate C(5,1) = 5 bipartitions
        CHECK(bipartitions.size() == 5);

        // Check that each bipartition has block1 of size 1
        for (const auto& [block1, block2] : bipartitions) {
            CHECK(block1.size() == 1);
            CHECK(block2.size() == 4);
        }
    }
}

TEST_CASE("Set bipartition properties") {
    SUBCASE("Complement property") {
        // For each bipartition (A,B), there should be a corresponding (B,A)
        // in the complete generation (but not in k-size constrained generation)
        std::vector<std::pair<std::vector<int>, std::vector<int>>> bipartitions;

        for (auto bipart : ecgen::set_bipart_gen(4)) {
            bipartitions.push_back(bipart);
        }

        // Create set of bipartitions (as sets for comparison)
        std::set<std::pair<std::set<int>, std::set<int>>> bipart_set;
        for (const auto& [block1, block2] : bipartitions) {
            bipart_set.insert({
                std::set<int>(block1.begin(), block1.end()),
                std::set<int>(block2.begin(), block2.end())
            });
        }

        // Check complement property
        for (const auto& [block1, block2] : bipart_set) {
            // The complement should also be in the set
            auto complement = std::make_pair(block2, block1);
            CHECK(bipart_set.find(complement) != bipart_set.end());
        }
    }
}
