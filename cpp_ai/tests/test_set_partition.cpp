#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "doctest.h"
#include "ecgen/set_partition.hpp"
#include <vector>
#include <algorithm>
#include <set>

TEST_CASE("Stirling numbers of the second kind") {
    SUBCASE("Basic Stirling numbers") {
        CHECK(ecgen::stirling2nd(4, 1) == 1);
        CHECK(ecgen::stirling2nd(4, 2) == 7);
        CHECK(ecgen::stirling2nd(4, 3) == 6);
        CHECK(ecgen::stirling2nd(4, 4) == 1);
    }
    
    SUBCASE("Edge cases") {
        CHECK(ecgen::stirling2nd(0, 0) == 1);
        CHECK(ecgen::stirling2nd(5, 0) == 0);
        CHECK(ecgen::stirling2nd(5, 6) == 0);
    }
}

TEST_CASE("Set partition generation") {
    SUBCASE("Partitions of [3]") {
        std::vector<std::vector<int>> partitions;
        
        for (auto& partition : ecgen::set_partition_gen(3)) {
            partitions.push_back(partition);
        }
        
        // Bell number B(3) = 5
        CHECK(partitions.size() == 5);
        
        // Check RG strings for partitions of [3]
        std::set<std::vector<int>> expected = {
            {0, 0, 0},  // {1,2,3}
            {0, 0, 1},  // {1,2},{3}
            {0, 1, 0},  // {1,3},{2}
            {0, 1, 1},  // {1},{2,3}
            {0, 1, 2}   // {1},{2},{3}
        };
        
        std::set<std::vector<int>> actual(partitions.begin(), partitions.end());
        CHECK(actual == expected);
    }
    
    SUBCASE("Partitions of [4] with 2 blocks") {
        std::vector<std::vector<int>> partitions;
        
        for (auto& partition : ecgen::set_partition_k_gen(4, 2)) {
            partitions.push_back(partition);
        }
        
        // S(4,2) = 7
        CHECK(partitions.size() == 7);
        
        // All partitions should have exactly 2 blocks
        for (const auto& partition : partitions) {
            std::set<int> blocks(partition.begin(), partition.end());
            CHECK(blocks.size() == 2);
        }
    }
}

TEST_CASE("Bell numbers") {
    SUBCASE("Small Bell numbers") {
        CHECK(ecgen::bell(0) == 1);
        CHECK(ecgen::bell(1) == 1);
        CHECK(ecgen::bell(2) == 2);
        CHECK(ecgen::bell(3) == 5);
        CHECK(ecgen::bell(4) == 15);
        CHECK(ecgen::bell(5) == 52);
    }
}