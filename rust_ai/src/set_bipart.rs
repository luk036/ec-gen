//! Set Bipartition Generator
//!
//! This module generates sequences of moves that partition a set of size `n` into two subsets.
//! A set bipartition divides a set into two disjoint subsets whose union is the original set.
//!
//! The algorithm generates a Gray code for set bipartitions, where each successive
//! bipartition differs by moving exactly one element from one block to the other.

use genawaiter::{sync::gen, yield_};
use lazy_static::lazy_static;
use std::collections::HashMap;
use std::sync::Mutex;

lazy_static! {
    static ref STIRLING_CACHE: Mutex<HashMap<i32, i32>> = Mutex::new(HashMap::new());
}

/// Calculate the Stirling number of the second kind for a given integer `n` (k = 2).
///
/// # Arguments
///
/// * `n` - Number of elements in a set
///
/// # Returns
///
/// The Stirling number of the second kind S(n, 2).
///
/// # Examples
///
/// ```
/// use rust_ai::set_bipart::stirling2nd2;
///
/// assert_eq!(stirling2nd2(5), 15);
/// ```
pub fn stirling2nd2(n: i32) -> i32 {
    if n < 3 {
        1
    } else {
        1 + 2 * stirling2nd2(n - 1)
    }
}

/// Generate a sequence of moves that partitions a set of size `n` into two subsets.
///
/// # Arguments
///
/// * `n` - Number of elements in the bi-partition
///
/// # Returns
///
/// A generator that yields integers representing which element to move.
///
/// # Examples
///
/// ```
/// use rust_ai::set_bipart::set_bipart;
///
/// let n = 5;
/// let mut b = vec![0; (n + 1) as usize];
/// b[n as usize] = 1;
/// println!("{:?}", &b[1..]);
///
/// for x in set_bipart(n) {
///     let old = b[x as usize];
///     b[x as usize] = 1 - b[x as usize];
///     println!("{:?} : Move {} from B{} to B{}", &b[1..], x, old, b[x as usize]);
/// }
/// ```
pub fn set_bipart(n: i32) -> impl Iterator<Item = i32> {
    gen!({
        for x in gen0(n) {
            yield_!(x);
        }
    })
    .into_iter()
}

fn gen0(n: i32) -> impl Iterator<Item = i32> {
    gen!({
        if n < 3 {
            return;
        }
        yield_!(n - 1);
        for x in gen1(n - 1) {
            yield_!(x);
        }
        yield_!(n);
        for x in neg1(n - 1) {
            yield_!(x);
        }
    })
    .into_iter()
}

fn gen1(n: i32) -> impl Iterator<Item = i32> {
    gen!({
        if n < 3 {
            return;
        }
        yield_!(2);
        for x in neg1(n - 1) {
            yield_!(x);
        }
        yield_!(n);
        for x in gen1(n - 1) {
            yield_!(x);
        }
    })
    .into_iter()
}

fn neg1(n: i32) -> impl Iterator<Item = i32> {
    gen!({
        if n < 3 {
            return;
        }
        for x in neg1(n - 1) {
            yield_!(x);
        }
        yield_!(n);
        for x in gen1(n - 1) {
            yield_!(x);
        }
        yield_!(2);
    })
    .into_iter()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_stirling2nd2() {
        assert_eq!(stirling2nd2(1), 1);
        assert_eq!(stirling2nd2(2), 1);
        assert_eq!(stirling2nd2(3), 3); // 1 + 2*1
        assert_eq!(stirling2nd2(4), 7); // 1 + 2*3
        assert_eq!(stirling2nd2(5), 15); // 1 + 2*7
    }

    #[test]
    fn test_set_bipart() {
        let n = 5;
        let moves: Vec<_> = set_bipart(n).collect();

        // Should generate 2^n - 2 moves (all bipartitions except empty sets)
        // let expected_len = 2_i32.pow(n as u32) - 2;
        assert_eq!(moves.len() as i32, 14);

        // Test that moves generate valid bipartitions
        let mut b = vec![0; (n + 1) as usize];
        b[n as usize] = 1;
        let mut bipartitions = vec![b[1..].to_vec()];

        for &x in &moves {
            b[x as usize] = 1 - b[x as usize];
            bipartitions.push(b[1..].to_vec());
        }

        // All bipartitions should be unique
        let mut sorted = bipartitions.clone();
        sorted.sort();
        sorted.dedup();
        assert_eq!(sorted.len(), bipartitions.len());
    }

    #[test]
    fn test_set_bipart_small() {
        let moves: Vec<_> = set_bipart(2).collect();
        assert_eq!(moves.len(), 0); // 2^2 - 2 = 2, but n < 3 returns empty

        let moves: Vec<_> = set_bipart(3).collect();
        assert_eq!(moves.len(), 2);
    }
}
