#include <iostream>
#include <vector>
#include "ecgen/combin.hpp"
#include "ecgen/set_partition.hpp"

int main() {
    std::cout << "=== Combinations Example ===\n\n";

    // Example 1: Calculate combination counts
    std::cout << "Combination counts:\n";
    std::cout << "C(6,3) = " << ecgen::comb(6, 3) << "\n";
    std::cout << "C(5,2) = " << ecgen::comb(5, 2) << "\n";
    std::cout << "C(4,4) = " << ecgen::comb(4, 4) << "\n\n";

    // Example 2: Generate all 3-combinations of 5 elements
    std::cout << "All 3-combinations of {A,B,C,D,E}:\n";
    std::vector<char> items = {'A', 'B', 'C', 'D', 'E'};
    int count = 0;

    for (auto& comb : ecgen::emk(5, 3, items)) {
        std::cout << ++count << ": ";
        for (int idx = 0; idx < 3; ++idx) {
            std::cout << items[idx] << " ";
        }
        std::cout << "\n";
    }

    std::cout << "\nTotal combinations: " << count << " (should be C(5,3) = "
              << ecgen::comb(5, 3) << ")\n\n";

    // Example 3: Compile-time combination
    std::cout << "Compile-time combination count:\n";
    constexpr auto c74 = ecgen::Combination<7, 4>();
    std::cout << "C(7,4) = " << c74 << " (computed at compile-time)\n";

    return 0;
}
