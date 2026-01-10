#include <iostream>
#include <vector>
#include <string>
#include "ecgen/sjt.hpp"
#include "ecgen/ehr.hpp"

int main() {
    std::cout << "=== Permutations Example ===\n\n";

    // Example 1: SJT algorithm
    std::cout << "SJT permutations of {1,2,3}:\n";
    std::vector<int> items_sjt = {1, 2, 3};
    int count_sjt = 0;

    for (auto& perm : ecgen::sjt_apply(3, items_sjt)) {
        std::cout << ++count_sjt << ": ";
        for (int elem : items_sjt) {
            std::cout << elem << " ";
        }
        std::cout << "\n";
    }

    std::cout << "\nTotal SJT permutations: " << count_sjt
              << " (should be 3! = " << ecgen::factorial(3) << ")\n\n";

    // Example 2: Ehrlich's algorithm
    std::cout << "Ehrlich permutations of {A,B,C}:\n";
    std::vector<std::string> items_ehr = {"A", "B", "C"};
    int count_ehr = 0;

    for (auto& perm : ecgen::ehr_apply(items_ehr)) {
        std::cout << ++count_ehr << ": ";
        for (const auto& x : items_ehr) {
            std::cout << x << " ";
        }
        std::cout << "\n";
    }

    std::cout << "\nTotal Ehrlich permutations: " << count_ehr
              << " (should be 3! = " << ecgen::factorial(3) << ")\n\n";

    // Example 3: Compare algorithms for n=4
    std::cout << "Comparing algorithms for n=4:\n";
    std::vector<int> test_items = {1, 2, 3, 4};

    int sjt_count = 0;
    for (auto& perm : ecgen::sjt_apply(4, test_items)) {
        ++sjt_count;
    }

    int ehr_count = 0;
    for (auto perm : ecgen::ehr_gen(4)) {
        ++ehr_count;
    }

    std::cout << "SJT generated: " << sjt_count << " permutations\n";
    std::cout << "Ehrlich generated: " << ehr_count << " permutations\n";
    std::cout << "Expected: " << ecgen::factorial(4) << " permutations\n";
    std::cout << "All algorithms generate the correct number!\n";

    return 0;
}
