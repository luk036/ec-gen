//! Set Partition Generator
//!
//! This module generates all possible set partitions of a set of size `n` into `k` blocks.
//! A set partition divides a set into disjoint subsets (blocks) whose union is the original set.
//!
//! The algorithm generates a Gray code for set partitions, where each successive
//! partition differs by moving exactly one element from one block to another.

use genawaiter::{sync::gen, yield_};
use std::collections::HashMap;
use std::sync::Mutex;
use lazy_static::lazy_static;

lazy_static! {
    static ref STIRLING_CACHE: Mutex<HashMap<(i32, i32), i32>> = Mutex::new(HashMap::new());
}

/// Calculate the Stirling number of the second kind for given values of `n` and `k`.
///
/// # Arguments
///
/// * `n` - Total number of objects or elements in a set
/// * `k` - Number of non-empty subsets to form
///
/// # Returns
///
/// The Stirling number of the second kind S(n, k).
///
/// # Examples
///
/// ```
/// use rust_ai::set_partition::stirling2nd;
///
/// assert_eq!(stirling2nd(5, 2), 15);
/// ```
pub fn stirling2nd(n: i32, k: i32) -> i32 {
    if k >= n || k <= 1 {
        1
    } else {
        stirling2nd_recur(n, k)
    }
}

fn stirling2nd_recur(n: i32, k: i32) -> i32 {
    let key = (n, k);
    {
        let cache = STIRLING_CACHE.lock().unwrap();
        if let Some(&value) = cache.get(&key) {
            return value;
        }
    }
    
    let n_minus_1 = n - 1;
    let a = if k == 2 { 1 } else { stirling2nd_recur(n_minus_1, k - 1) };
    let b = if k == n_minus_1 { 1 } else { stirling2nd_recur(n_minus_1, k) };
    let result = a + k * b;
    
    {
        let mut cache = STIRLING_CACHE.lock().unwrap();
        cache.insert(key, result);
    }
    
    result
}

/// Generate all possible set partitions of a set of size `n` into `k` blocks.
///
/// # Arguments
///
/// * `n` - Total number of elements in the set
/// * `k` - Number of blocks in the set partition
///
/// # Returns
///
/// A generator that yields tuples `(x, y)` where `x` is the element to move
/// and `y` is the destination block.
///
/// # Examples
///
/// ```
/// use rust_ai::set_partition::set_partition;
///
/// let (n, k) = (5, 2);
/// let mut b = vec![0; (n - k + 1) as usize];
/// b.extend((0..k).collect::<Vec<_>>());
/// println!("{:?}", &b[1..]);
///
/// for (x, y) in set_partition(n, k) {
///     let old = b[x as usize];
///     b[x as usize] = y;
///     println!("{:?} : Move {} from block {} to {}", &b[1..], x, old, y);
/// }
/// ```
pub fn set_partition(n: i32, k: i32) -> impl Iterator<Item = (i32, i32)> {
    gen!({
        if !(k > 1 && k < n) {
            return;
        }
        if k % 2 == 0 {
            for pair in gen0_even(n, k) {
                yield_!(pair);
            }
        } else {
            for pair in gen0_odd(n, k) {
                yield_!(pair);
            }
        }
    })
    .into_iter()
}

fn gen0_even(n: i32, k: i32) -> impl Iterator<Item = (i32, i32)> {
    gen!({
        if k > 2 {
            for pair in gen0_odd(n - 1, k - 1) {
                yield_!(pair);
            }
        }
        yield_!((n - 1, k - 1));
        if k < n - 1 {
            for pair in gen1_even(n - 1, k) {
                yield_!(pair);
            }
            yield_!((n, k - 2));
            for pair in neg1_even(n - 1, k) {
                yield_!(pair);
            }
            for i in (1..=k - 3).rev().step_by(2) {
                yield_!((n, i));
                for pair in gen1_even(n - 1, k) {
                    yield_!(pair);
                }
                yield_!((n, i - 1));
                for pair in neg1_even(n - 1, k) {
                    yield_!(pair);
                }
            }
        } else {
            yield_!((n, k - 2));
            for i in (1..=k - 3).rev().step_by(2) {
                yield_!((n, i));
                yield_!((n, i - 1));
            }
        }
    })
    .into_iter()
}

fn neg0_even(n: i32, k: i32) -> impl Iterator<Item = (i32, i32)> {
    gen!({
        if k < n - 1 {
            for i in (1..=k - 3).step_by(2) {
                for pair in gen1_even(n - 1, k) {
                    yield_!(pair);
                }
                yield_!((n, i));
                for pair in neg1_even(n - 1, k) {
                    yield_!(pair);
                }
                yield_!((n, i + 1));
            }
            for pair in gen1_even(n - 1, k) {
                yield_!(pair);
            }
            yield_!((n, k - 1));
            for pair in neg1_even(n - 1, k) {
                yield_!(pair);
            }
        } else {
            for i in (1..=k - 3).step_by(2) {
                yield_!((n, i));
                yield_!((n, i + 1));
            }
            yield_!((n, k - 1));
        }
        yield_!((n - 1, 0));
        if k > 3 {
            for pair in neg0_odd(n - 1, k - 1) {
                yield_!(pair);
            }
        }
    })
    .into_iter()
}

fn gen1_even(n: i32, k: i32) -> impl Iterator<Item = (i32, i32)> {
    gen!({
        if k > 3 {
            for pair in gen1_odd(n - 1, k - 1) {
                yield_!(pair);
            }
        }
        yield_!((k, k - 1));
        if k < n - 1 {
            for pair in neg1_even(n - 1, k) {
                yield_!(pair);
            }
            yield_!((n, k - 2));
            for pair in gen1_even(n - 1, k) {
                yield_!(pair);
            }
            for i in (1..=k - 3).rev().step_by(2) {
                yield_!((n, i));
                for pair in neg1_even(n - 1, k) {
                    yield_!(pair);
                }
                yield_!((n, i - 1));
                for pair in gen1_even(n - 1, k) {
                    yield_!(pair);
                }
            }
        } else {
            yield_!((n, k - 2));
            for i in (1..=k - 3).rev().step_by(2) {
                yield_!((n, i));
                yield_!((n, i - 1));
            }
        }
    })
    .into_iter()
}

fn neg1_even(n: i32, k: i32) -> impl Iterator<Item = (i32, i32)> {
    gen!({
        if k < n - 1 {
            for i in (1..=k - 3).step_by(2) {
                for pair in neg1_even(n - 1, k) {
                    yield_!(pair);
                }
                yield_!((n, i));
                for pair in gen1_even(n - 1, k) {
                    yield_!(pair);
                }
                yield_!((n, i + 1));
            }
            for pair in neg1_even(n - 1, k) {
                yield_!(pair);
            }
            yield_!((n, k - 1));
            for pair in gen1_even(n - 1, k) {
                yield_!(pair);
            }
        } else {
            for i in (1..=k - 3).step_by(2) {
                yield_!((n, i));
                yield_!((n, i + 1));
            }
            yield_!((n, k - 1));
        }
        yield_!((k, 0));
        if k > 3 {
            for pair in neg1_odd(n - 1, k - 1) {
                yield_!(pair);
            }
        }
    })
    .into_iter()
}

fn gen0_odd(n: i32, k: i32) -> impl Iterator<Item = (i32, i32)> {
    gen!({
        for pair in gen1_even(n - 1, k - 1) {
            yield_!(pair);
        }
        yield_!((k, k - 1));
        if k < n - 1 {
            for pair in neg1_odd(n - 1, k) {
                yield_!(pair);
            }
            for i in (2..=k - 2).rev().step_by(2) {
                yield_!((n, i));
                for pair in gen1_odd(n - 1, k) {
                    yield_!(pair);
                }
                yield_!((n, i - 1));
                for pair in neg1_odd(n - 1, k) {
                    yield_!(pair);
                }
            }
        } else {
            for i in (2..=k - 2).rev().step_by(2) {
                yield_!((n, i));
                yield_!((n, i - 1));
            }
        }
    })
    .into_iter()
}

fn neg0_odd(n: i32, k: i32) -> impl Iterator<Item = (i32, i32)> {
    gen!({
        if k < n - 1 {
            for i in (1..=k - 2).step_by(2) {
                for pair in gen1_odd(n - 1, k) {
                    yield_!(pair);
                }
                yield_!((n, i));
                for pair in neg1_odd(n - 1, k) {
                    yield_!(pair);
                }
                yield_!((n, i + 1));
            }
            for pair in gen1_odd(n - 1, k) {
                yield_!(pair);
            }
        } else {
            for i in (1..=k - 2).step_by(2) {
                yield_!((n, i));
                yield_!((n, i + 1));
            }
        }
        yield_!((k, 0));
        for pair in neg1_even(n - 1, k - 1) {
            yield_!(pair);
        }
    })
    .into_iter()
}

fn gen1_odd(n: i32, k: i32) -> impl Iterator<Item = (i32, i32)> {
    gen!({
        for pair in gen0_even(n - 1, k - 1) {
            yield_!(pair);
        }
        yield_!((n - 1, k - 1));
        if k < n - 1 {
            for pair in gen1_odd(n - 1, k) {
                yield_!(pair);
            }
            for i in (2..=k - 2).rev().step_by(2) {
                yield_!((n, i));
                for pair in neg1_odd(n - 1, k) {
                    yield_!(pair);
                }
                yield_!((n, i - 1));
                for pair in gen1_odd(n - 1, k) {
                    yield_!(pair);
                }
            }
        } else {
            for i in (2..=k - 2).rev().step_by(2) {
                yield_!((n, i));
                yield_!((n, i - 1));
            }
        }
    })
    .into_iter()
}

fn neg1_odd(n: i32, k: i32) -> impl Iterator<Item = (i32, i32)> {
    gen!({
        if k < n - 1 {
            for i in (1..=k - 2).step_by(2) {
                for pair in neg1_odd(n - 1, k) {
                    yield_!(pair);
                }
                yield_!((n, i));
                for pair in gen1_odd(n - 1, k) {
                    yield_!(pair);
                }
                yield_!((n, i + 1));
            }
            for pair in neg1_odd(n - 1, k) {
                yield_!(pair);
            }
        } else {
            for i in (1..=k - 2).step_by(2) {
                yield_!((n, i));
                yield_!((n, i + 1));
            }
        }
        yield_!((n - 1, 0));
        for pair in neg0_even(n - 1, k - 1) {
            yield_!(pair);
        }
    })
    .into_iter()
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_stirling2nd() {
        assert_eq!(stirling2nd(5, 2), 15);
        assert_eq!(stirling2nd(4, 2), 7);
        assert_eq!(stirling2nd(3, 2), 3);
        assert_eq!(stirling2nd(2, 2), 1);
        assert_eq!(stirling2nd(1, 1), 1);
    }
    
    #[test]
    fn test_set_partition_small() {
        let moves: Vec<_> = set_partition(5, 2).collect();
        assert_eq!(moves.len(), 14); // S(5,2) - 1 moves
        
        // Test that moves generate valid partitions
        let (n, k) = (5, 2);
        let mut b = vec![0; (n - k + 1) as usize];
        b.extend((0..k).collect::<Vec<_>>());
        let mut partitions = vec![b[1..].to_vec()];
        
        for &(x, y) in &moves {
            b[x as usize] = y;
            partitions.push(b[1..].to_vec());
        }
        
        // Should generate S(5,2) = 15 partitions
        assert_eq!(partitions.len(), 15);
        
        // All partitions should be unique
        let mut sorted = partitions.clone();
        sorted.sort();
        sorted.dedup();
        assert_eq!(sorted.len(), 15);
    }
    
    #[test]
    fn test_set_partition_edge_cases() {
        // k >= n should return empty
        let moves: Vec<_> = set_partition(5, 5).collect();
        assert_eq!(moves.len(), 0);
        
        // k <= 1 should return empty
        let moves: Vec<_> = set_partition(5, 1).collect();
        assert_eq!(moves.len(), 0);
        
        // n < k should return empty
        let moves: Vec<_> = set_partition(3, 5).collect();
        assert_eq!(moves.len(), 0);
    }
}
