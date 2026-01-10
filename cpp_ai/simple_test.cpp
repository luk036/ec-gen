#include <iostream>
#include "ecgen/combin.hpp"

int main() {
    std::cout << "Testing ecgen C++ library\n";

    // Test combination count
    std::cout << "C(6,3) = " << ecgen::comb(6, 3) << "\n";
    std::cout << "C(5,2) = " << ecgen::comb(5, 2) << "\n";

    // Test compile-time combination
    constexpr auto c42 = ecgen::Combination<4, 2>();
    std::cout << "C(4,2) at compile time = " << c42 << "\n";

    return 0;
}
