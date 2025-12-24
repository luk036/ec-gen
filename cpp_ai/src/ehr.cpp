#include "ecgen/ehr.hpp"
#include <algorithm>

namespace ecgen {

    auto ehr_gen(int num) -> cppcoro::generator<std::vector<int>> {
        if (num <= 0) {
            co_return;
        }
        
        std::vector<int> perm(num);
        for (int idx = 0; idx < num; ++idx) {
            perm[idx] = idx + 1;
        }
        
        std::vector<int> c(num, 0);
        std::vector<int> o(num, 1);
        
        co_yield perm;
        
        while (true) {
            int pos = num - 1;
            int sum = 0;
            
            // Determine next permutation
            int quot = c[pos] + o[pos];
            while (quot < 0 || quot == pos + 1) {
                if (quot == pos + 1) {
                    if (pos == 0) {
                        co_return; // All permutations generated
                    }
                    sum += 1;
                }
                o[pos] = -o[pos];
                pos -= 1;
                quot = c[pos] + o[pos];
            }
            
            // Swap elements
            std::swap(perm[pos - c[pos] + sum], perm[pos - quot + sum]);
            c[pos] = quot;
            
            co_yield perm;
        }
    }

} // namespace ecgen