//! Steinhaus-Johnson-Trotter Algorithm
//!
//! This module implements the Steinhaus-Johnson-Trotter algorithm for generating
//! all possible permutations (arrangements) of a set of items.
//!
//! The algorithm generates a sequence of swaps that, when applied to a list,
//! will produce all possible permutations of that list. Each new permutation
//! differs from the previous one by just a single swap of adjacent elements.

use genawaiter::{sync::gen, yield_};

/// Generate all permutations of length `n` using the Steinhaus-Johnson-Trotter algorithm.
///
/// Note: The list returns to the original permutation after all swaps.
///
/// # Arguments
///
/// * `n` - Number of elements in the permutation
///
/// # Returns
///
/// A generator that yields integers representing positions where swaps should occur.
///
/// # Examples
///
/// ```
/// use rust_ai::sjt::sjt_gen;
///
/// let mut perm = vec!["🍉", "🍌", "🍇", "🍏"];
/// for x in sjt_gen(4) {
///     println!("{}", perm.join(""));
///     perm.swap(x as usize, x as usize + 1);
/// }
/// ```
pub fn sjt_gen(n: i32) -> impl Iterator<Item = i32> {
    gen!({
        if n == 2 {
            yield_!(0);
            yield_!(0); // tricky part: return to the origin
            return;
        }

        let up: Vec<i32> = (0..n - 1).collect();
        let down: Vec<i32> = (0..n - 1).rev().collect();
        let mut gen = sjt_gen(n - 1);

        while let Some(x) = gen.next() {
            for &i in down.iter() {
                yield_!(i);
            }
            yield_!(x + 1);
            for &i in up.iter() {
                yield_!(i);
            }
            if let Some(next_x) = gen.next() {
                yield_!(next_x);
            }
        }
    })
    .into_iter()
}

/// Generate the swaps for the Steinhaus-Johnson-Trotter algorithm (original method).
///
/// # Arguments
///
/// * `n` - Number of elements in the permutation
///
/// # Returns
///
/// A generator that yields integers representing positions where swaps should occur.
///
/// # Examples
///
/// ```
/// use rust_ai::sjt::plain_changes;
///
/// let mut perm = vec!["🍉", "🍌", "🍇", "🍏"];
/// for x in plain_changes(4) {
///     println!("{}", perm.join(""));
///     perm.swap(x as usize, x as usize + 1);
/// }
/// ```
pub fn plain_changes(n: i32) -> impl Iterator<Item = i32> {
    gen!({
        if n < 1 {
            return;
        }

        let up: Vec<i32> = (0..n - 1).collect();
        let down: Vec<i32> = (0..n - 1).rev().collect();
        let mut recur = plain_changes(n - 1);

        loop {
            for &x in down.iter() {
                yield_!(x);
            }
            match recur.next() {
                Some(x) => yield_!(x + 1),
                None => break,
            }
            for &x in up.iter() {
                yield_!(x);
            }
            match recur.next() {
                Some(x) => yield_!(x),
                None => break,
            }
        }
    })
    .into_iter()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_sjt_gen_small() {
        let swaps: Vec<_> = sjt_gen(2).collect();
        assert_eq!(swaps, vec![0, 0]);

        let swaps: Vec<_> = sjt_gen(3).collect();
        // For n=3, should generate 3! = 6 swaps
        assert_eq!(swaps.len(), 6);
    }

    #[test]
    fn test_sjt_gen_permutations() {
        let n = 4;
        let mut perm: Vec<i32> = (0..n).collect();
        let mut permutations = vec![perm.clone()];

        for swap_idx in sjt_gen(n) {
            perm.swap(swap_idx as usize, swap_idx as usize + 1);
            permutations.push(perm.clone());
        }

        // Should generate n! + 1 permutations (return to the start)
        assert_eq!(permutations.len(), 25); // 4! + 1 = 25

        // All permutations should be unique
        let mut sorted = permutations.clone();
        sorted.sort();
        sorted.dedup();
        assert_eq!(sorted.len(), 24);

        // Should return to original permutation
        assert_eq!(perm, vec![0, 1, 2, 3]);
    }

    #[test]
    fn test_plain_changes_small() {
        let swaps: Vec<_> = plain_changes(2).collect();
        // For n=2, should generate 1 swap
        assert_eq!(swaps.len(), 1);

        let swaps: Vec<_> = plain_changes(3).collect();
        // For n=3, should generate 3! - 1 = 5 swaps
        assert_eq!(swaps.len(), 5);
    }

    #[test]
    fn test_plain_changes_permutations() {
        let n = 4;
        let mut perm: Vec<i32> = (0..n).collect();
        let mut permutations = vec![perm.clone()];

        for swap_idx in plain_changes(n) {
            perm.swap(swap_idx as usize, swap_idx as usize + 1);
            permutations.push(perm.clone());
        }

        // Should generate n! permutations
        assert_eq!(permutations.len(), 24); // 4! = 24

        // All permutations should be unique
        let mut sorted = permutations.clone();
        sorted.sort();
        sorted.dedup();
        assert_eq!(sorted.len(), 24);
    }

    #[test]
    fn test_adjacent_swaps() {
        let n = 4;
        let swaps: Vec<_> = sjt_gen(n).collect();

        // All swaps should be between adjacent elements
        for &swap_idx in &swaps {
            assert!(swap_idx >= 0 && swap_idx < n - 1);
        }

        // Consecutive permutations should differ by exactly one adjacent swap
        let mut perm: Vec<i32> = (0..n).collect();
        let mut prev_perm = perm.clone();

        for &swap_idx in &swaps {
            perm.swap(swap_idx as usize, swap_idx as usize + 1);

            // Count differences
            let diff_count = prev_perm
                .iter()
                .zip(perm.iter())
                .filter(|(a, b)| a != b)
                .count();

            assert_eq!(
                diff_count, 2,
                "Should differ by exactly 2 elements (one swap)"
            );
            prev_perm = perm.clone();
        }
    }
}
