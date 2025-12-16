//! Skeleton module with example functions.
//!
//! This module serves as a starting point and contains example functions.

/// Calculate the n-th Fibonacci number.
///
/// # Arguments
///
/// * `n` - The position in the Fibonacci sequence (1-based)
///
/// # Returns
///
/// The n-th Fibonacci number.
///
/// # Examples
///
/// ```
/// use rust_ai::skeleton::fib;
///
/// assert_eq!(fib(1), 1);
/// assert_eq!(fib(2), 1);
/// assert_eq!(fib(3), 2);
/// assert_eq!(fib(4), 3);
/// assert_eq!(fib(5), 5);
/// ```
pub fn fib(n: u32) -> u64 {
    assert!(n > 0, "n must be positive");
    let mut a = 1;
    let mut b = 1;
    for _ in 0..n - 1 {
        let next = a + b;
        a = b;
        b = next;
    }
    a
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_fib() {
        assert_eq!(fib(1), 1);
        assert_eq!(fib(2), 1);
        assert_eq!(fib(3), 2);
        assert_eq!(fib(4), 3);
        assert_eq!(fib(5), 5);
        assert_eq!(fib(6), 8);
        assert_eq!(fib(7), 13);
        assert_eq!(fib(8), 21);
    }
    
    #[test]
    #[should_panic(expected = "n must be positive")]
    fn test_fib_zero() {
        fib(0);
    }
}
