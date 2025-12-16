#include "ecgen/ehr.hpp"
#include <algorithm>

namespace ecgen {

    auto ehr_gen(int n) -> cppcoro::generator<std::vector<int>> {
        if (n <= 0) {
            co_return;
        }
        
        std::vector<int> perm(n);
        for (int i = 0; i < n; ++i) {
            perm[i] = i + 1;
        }
        
        std::vector<int> c(n, 0);
        std::vector<int> o(n, 1);
        
        co_yield perm;
        
        while (true) {
            int j = n - 1;
            int s = 0;
            
            // Determine next permutation
            int q = c[j] + o[j];
            while (q < 0 || q == j + 1) {
                if (q == j + 1) {
                    if (j == 0) {
                        co_return; // All permutations generated
                    }
                    s += 1;
                }
                o[j] = -o[j];
                j -= 1;
                q = c[j] + o[j];
            }
            
            // Swap elements
            std::swap(perm[j - c[j] + s], perm[j - q + s]);
            c[j] = q;
            
            co_yield perm;
        }
    }

} // namespace ecgen