#include "ecgen/set_partition.hpp"
#include <algorithm>
#include <stack>

namespace ecgen {

    auto set_partition_gen(int n) -> cppcoro::generator<std::vector<int>> {
        if (n <= 0) {
            co_return;
        }
        
        std::vector<int> a(n, 0);  // RG string
        std::vector<int> b(n, 1);  // Maximum block index + 1
        std::vector<int> m(n + 1, 0);  // Helper array
        
        // Initial partition: all elements in block 0
        co_yield a;
        
        int j = n - 1;
        while (j > 0) {
            int v = b[j] + a[j];
            
            if (v <= m[j]) {
                a[j] = v;
                
                if (v == m[j]) {
                    m[j + 1] = std::max(m[j], v + 1);
                } else {
                    m[j + 1] = m[j];
                }
                
                if (a[j] == b[j]) {
                    b[j + 1] = b[j] + 1;
                } else {
                    b[j + 1] = b[j];
                }
                
                j = n - 1;
                co_yield a;
            } else {
                --j;
            }
        }
    }

    auto set_partition_k_gen(int n, int k) -> cppcoro::generator<std::vector<int>> {
        if (k <= 0 || k > n) {
            co_return;
        }
        
        std::vector<int> a(n, 0);  // RG string
        std::vector<int> b(n, 1);  // Maximum block index + 1
        std::vector<int> m(n + 1, 0);  // Helper array
        
        // Initialize for exactly k blocks
        for (int i = 0; i < k; ++i) {
            a[i] = i;
            b[i] = i + 1;
            m[i] = i;
        }
        for (int i = k; i < n; ++i) {
            a[i] = k - 1;
            b[i] = k;
            m[i] = k - 1;
        }
        m[n] = k - 1;
        
        co_yield a;
        
        int j = n - 1;
        while (j > 0) {
            int v = b[j] + a[j];
            
            if (v <= m[j] && v < k) {
                a[j] = v;
                
                if (v == m[j]) {
                    m[j + 1] = std::max(m[j], v + 1);
                } else {
                    m[j + 1] = m[j];
                }
                
                if (a[j] == b[j]) {
                    b[j + 1] = b[j] + 1;
                } else {
                    b[j + 1] = b[j];
                }
                
                j = n - 1;
                co_yield a;
            } else {
                --j;
            }
        }
    }

} // namespace ecgen