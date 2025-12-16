//! Skeleton Module
//!
//! This is a skeleton module that can serve as a starting point.
//! It includes a Fibonacci function example and basic structure.

/// Calculate the n-th Fibonacci number.
///
/// # Arguments
///
/// * `n` - Position in the Fibonacci sequence (1-based)
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
/// assert_eq!(fib(5), 5);
/// assert_eq!(fib(1), 1);
/// assert_eq!(fib(2), 1);
/// ```
pub fn fib(n: u32) -> u64 {
    assert!(n > 0, "n must be positive");
    let (mut a, mut b) = (1, 1);
    for _ in 0..n - 1 {
        (a, b) = (b, a + b);
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

    #[test]
    fn test_fib_large() {
        // Test that it doesn't overflow for reasonable values
        assert_eq!(fib(20), 6765);
        assert_eq!(fib(30), 832040);
    }
}
