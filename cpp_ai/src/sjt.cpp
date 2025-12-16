#include "ecgen/sjt.hpp"
#include <algorithm>
#include <stack>

namespace ecgen {

    auto sjt_gen(int n) -> cppcoro::generator<int> {
        if (n <= 1) {
            co_return;
        }
        
        // Recursive implementation
        struct frame {
            int n;
            int dir;
            int i;
        };
        
        std::stack<frame> stk;
        stk.push({n, -1, 0});
        
        while (!stk.empty()) {
            auto& f = stk.top();
            
            if (f.i == 0) {
                // First visit: setup for this level
                if (f.n == 2) {
                    // Base case
                    co_yield 0;
                    stk.pop();
                    continue;
                }
                
                // Push recursive call for n-1
                stk.push({f.n - 1, -1, 0});
                f.i = 1;
            } else if (f.i <= f.n - 1) {
                // Generate swaps for this level
                if (f.dir < 0) {
                    // Moving left to right
                    for (int j = 0; j < f.n - 1; ++j) {
                        co_yield j;
                    }
                } else {
                    // Moving right to left
                    for (int j = f.n - 2; j >= 0; --j) {
                        co_yield j;
                    }
                }
                
                // Swap direction for next iteration
                f.dir = -f.dir;
                ++f.i;
                
                if (f.i <= f.n - 1) {
                    // Push recursive call again
                    stk.push({f.n - 1, -1, 0});
                }
            } else {
                // Done with this level
                stk.pop();
            }
        }
    }

    auto plain_changes(int n) -> cppcoro::generator<int> {
        if (n <= 1) {
            co_return;
        }
        
        // Alternative implementation using different recursion
        auto helper = [](int n, int dir, auto& self) -> cppcoro::generator<int> {
            if (n == 2) {
                co_yield 0;
                co_return;
            }
            
            for (int i = 0; i < n - 1; ++i) {
                for (int swap_pos : self(n - 1, -1, self)) {
                    co_yield swap_pos;
                }
                
                if (dir < 0) {
                    co_yield i;
                } else {
                    co_yield n - 2 - i;
                }
            }
            
            for (int swap_pos : self(n - 1, 1, self)) {
                co_yield swap_pos;
            }
        };
        
        for (int swap_pos : helper(n, -1, helper)) {
            co_yield swap_pos;
        }
    }

} // namespace ecgen