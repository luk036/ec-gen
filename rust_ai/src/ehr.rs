//! Ehrlich-Hopcroft-Reingold (EHR) Algorithm
//!
//! This module implements the Ehrlich-Hopcroft-Reingold algorithm for generating permutations.
//! A permutation is a way of arranging a set of items in a different order.
//!
//! The algorithm efficiently generates all possible permutations of a given length
//! by yielding the index of the element that should be swapped with the first element
//! (index 0) to create each new permutation.
//!
//! The algorithm uses two lists: `b` represents the current permutation,
//! while `c` keeps track of the algorithm's state. The function enters a loop
//! where it updates these lists according to specific rules, generating a new
//! permutation with each iteration.

use genawaiter::{sync::gen, yield_};

/// Generate all permutations of length `n` using the EHR algorithm.
///
/// Yields the indices of the elements to be swapped with the first element
/// (index 0) in each permutation.
///
/// # Arguments
///
/// * `n` - Number of elements in the permutation
///
/// # Returns
///
/// A generator that yields integers representing swap indices.
///
/// # Examples
///
/// ```
/// use rust_ai::ehr::ehr_gen;
///
/// for i in ehr_gen(4) {
///     println!("swap 0 and {}", i);
/// }
/// ```
pub fn ehr_gen(n: i32) -> impl Iterator<Item = i32> {
    gen!({
        if n < 2 {
            return;
        }

        let mut b: Vec<i32> = (0..n).collect(); // b[0] is never used
        let mut c: Vec<i32> = vec![0; (n + 1) as usize]; // c[0] is never used

        loop {
            let mut k = 1;
            loop {
                if c[k as usize] == k {
                    c[k as usize] = 0;
                    k += 1;
                }
                if c[k as usize] < k {
                    break;
                }
            }
            if k == n {
                break;
            }
            c[k as usize] += 1;
            yield_!(b[k as usize]);

            // Reverse b[1..k]
            let slice_len = k as usize;
            if slice_len > 1 {
                let mut left = 1;
                let mut right = slice_len - 1;
                while left < right {
                    b.swap(left, right);
                    left += 1;
                    right -= 1;
                }
            }
        }
    })
    .into_iter()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_ehr_gen() {
        let swaps: Vec<_> = ehr_gen(4).collect();
        assert_eq!(swaps.len(), 23); // 4! - 1 swaps

        // Check first few swaps
        assert_eq!(swaps[0], 1);
        assert_eq!(swaps[1], 2);
        assert_eq!(swaps[2], 1);
    }

    #[test]
    fn test_ehr_gen_small() {
        let swaps: Vec<_> = ehr_gen(2).collect();
        assert_eq!(swaps, vec![1]);

        let swaps: Vec<_> = ehr_gen(1).collect();
        assert_eq!(swaps.len(), 0);

        let swaps: Vec<_> = ehr_gen(0).collect();
        assert_eq!(swaps.len(), 0);
    }

    #[test]
    fn test_ehr_gen_permutations() {
        let n = 3;
        let mut perm: Vec<i32> = (0..n).collect();
        let mut permutations = vec![perm.clone()];

        for swap_idx in ehr_gen(n) {
            perm.swap(0, swap_idx as usize);
            permutations.push(perm.clone());
        }

        // Should generate n! permutations
        assert_eq!(permutations.len(), 6); // 3! = 6

        // All permutations should be unique
        let mut sorted = permutations.clone();
        sorted.sort();
        sorted.dedup();
        assert_eq!(sorted.len(), 6);
    }
}
