#include "ecgen/set_partition.hpp"
#include <algorithm>
#include <stack>

namespace ecgen {

    auto set_partition_gen(int num) -> cppcoro::generator<std::vector<int>> {
        if (num <= 0) {
            co_return;
        }

        std::vector<int> a(num, 0);  // RG string
        std::vector<int> b(num, 1);  // Maximum block index + 1
        std::vector<int> m(num + 1, 0);  // Helper array

        // Initial partition: all elements in block 0
        co_yield a;

        int pos = num - 1;
        while (pos > 0) {
            int val = b[pos] + a[pos];

            if (val <= m[pos]) {
                a[pos] = val;

                if (val == m[pos]) {
                    m[pos + 1] = std::max(m[pos], val + 1);
                } else {
                    m[pos + 1] = m[pos];
                }

                if (a[pos] == b[pos]) {
                    b[pos + 1] = b[pos] + 1;
                } else {
                    b[pos + 1] = b[pos];
                }

                pos = num - 1;
                co_yield a;
            } else {
                --pos;
            }
        }
    }

    auto set_partition_k_gen(int num, int select) -> cppcoro::generator<std::vector<int>> {
        if (select <= 0 || select > num) {
            co_return;
        }

        std::vector<int> a(num, 0);  // RG string
        std::vector<int> b(num, 1);  // Maximum block index + 1
        std::vector<int> m(num + 1, 0);  // Helper array

        // Initialize for exactly select blocks
        for (int idx = 0; idx < select; ++idx) {
            a[idx] = idx;
            b[idx] = idx + 1;
            m[idx] = idx;
        }
        for (int idx = select; idx < num; ++idx) {
            a[idx] = select - 1;
            b[idx] = select;
            m[idx] = select - 1;
        }
        m[num] = select - 1;

        co_yield a;

        int pos = num - 1;
        while (pos > 0) {
            int val = b[pos] + a[pos];

            if (val <= m[pos] && val < select) {
                a[pos] = val;

                if (val == m[pos]) {
                    m[pos + 1] = std::max(m[pos], val + 1);
                } else {
                    m[pos + 1] = m[pos];
                }

                if (a[pos] == b[pos]) {
                    b[pos + 1] = b[pos] + 1;
                } else {
                    b[pos + 1] = b[pos];
                }

                pos = num - 1;
                co_yield a;
            } else {
                --pos;
            }
        }
    }

} // namespace ecgen
