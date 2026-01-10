#include "ecgen/sjt.hpp"
#include <algorithm>
#include <stack>

namespace ecgen {

    auto sjt_gen(int num) -> cppcoro::generator<int> {
        if (num <= 1) {
            co_return;
        }

        // Recursive implementation
        struct frame {
            int n;
            int dir;
            int state;
        };

        std::stack<frame> stk;
        stk.push({num, -1, 0});

        while (!stk.empty()) {
            auto& frame = stk.top();

            if (frame.state == 0) {
                // First visit: setup for this level
                if (frame.n == 2) {
                    // Base case
                    co_yield 0;
                    stk.pop();
                    continue;
                }

                // Push recursive call for n-1
                stk.push({frame.n - 1, -1, 0});
                frame.state = 1;
            } else if (frame.state <= frame.n - 1) {
                // Generate swaps for this level
                if (frame.dir < 0) {
                    // Moving left to right
                    for (int pos = 0; pos < frame.n - 1; ++pos) {
                        co_yield pos;
                    }
                } else {
                    // Moving right to left
                    for (int pos = frame.n - 2; pos >= 0; --pos) {
                        co_yield pos;
                    }
                }

                // Swap direction for next iteration
                frame.dir = -frame.dir;
                ++frame.state;

                if (frame.state <= frame.n - 1) {
                    // Push recursive call again
                    stk.push({frame.n - 1, -1, 0});
                }
            } else {
                // Done with this level
                stk.pop();
            }
        }
    }

    auto plain_changes(int num) -> cppcoro::generator<int> {
        if (num <= 1) {
            co_return;
        }

        // Alternative implementation using different recursion
        auto helper = [](int n, int dir, auto& self) -> cppcoro::generator<int> {
            if (n == 2) {
                co_yield 0;
                co_return;
            }

            for (int idx = 0; idx < n - 1; ++idx) {
                for (int swap_pos : self(n - 1, -1, self)) {
                    co_yield swap_pos;
                }

                if (dir < 0) {
                    co_yield idx;
                } else {
                    co_yield n - 2 - idx;
                }
            }

            for (int swap_pos : self(n - 1, 1, self)) {
                co_yield swap_pos;
            }
        };

        for (int swap_pos : helper(num, -1, helper)) {
            co_yield swap_pos;
        }
    }

} // namespace ecgen
