//! Gray Code Generator
//!
//! This module implements a Gray code generator, which is a sequence of binary numbers
//! where each successive number differs from the previous one by only one bit.

/// Generate a sequence of binary reflected Gray code numbers up to a given length `n`.
///
/// # Arguments
///
/// * `n` - The number of bits in the binary reflected Gray code sequence
///
/// # Returns
///
/// An iterator that yields integers representing which bit to flip.
///
/// # Examples
///
/// ```
/// use rust_ai::gray_code::brgc_gen;
///
/// let mut generator = brgc_gen(4);
/// assert_eq!(generator.next(), Some(0));
/// assert_eq!(generator.next(), Some(1));
/// assert_eq!(generator.next(), Some(0));
/// assert_eq!(generator.next(), Some(2));
/// ```
pub fn brgc_gen(n: u32) -> impl Iterator<Item = u32> {
    // Simple recursive implementation
    BrgcGen::new(n)
}

struct BrgcGen {
    n: u32,
    state: BrgcGenState,
}

enum BrgcGenState {
    Start,
    FirstPart(Box<dyn Iterator<Item = u32>>),
    Middle,
    SecondPart(Box<dyn Iterator<Item = u32>>),
    Done,
}

impl BrgcGen {
    fn new(n: u32) -> Self {
        Self {
            n,
            state: BrgcGenState::Start,
        }
    }
}

impl Iterator for BrgcGen {
    type Item = u32;
    
    fn next(&mut self) -> Option<Self::Item> {
        match &mut self.state {
            BrgcGenState::Start => {
                if self.n == 1 {
                    self.state = BrgcGenState::Middle;
                    Some(0)
                } else {
                    self.state = BrgcGenState::FirstPart(Box::new(brgc_gen(self.n - 1)));
                    self.next()
                }
            }
            BrgcGenState::FirstPart(iter) => {
                if let Some(item) = iter.next() {
                    Some(item)
                } else {
                    self.state = BrgcGenState::Middle;
                    Some(self.n - 1)
                }
            }
            BrgcGenState::Middle => {
                if self.n == 1 {
                    self.state = BrgcGenState::Done;
                    None
                } else {
                    self.state = BrgcGenState::SecondPart(Box::new(brgc_gen(self.n - 1)));
                    self.next()
                }
            }
            BrgcGenState::SecondPart(iter) => iter.next(),
            BrgcGenState::Done => None,
        }
    }
}

/// Generate a binary reflected Gray code sequence of length `n`.
///
/// # Arguments
///
/// * `n` - The number of bits in the binary code
///
/// # Returns
///
/// An iterator that yields vectors of bits (0 or 1).
///
/// # Examples
///
/// ```
/// use rust_ai::gray_code::brgc;
///
/// let codes: Vec<Vec<u8>> = brgc(3).collect();
/// assert_eq!(codes[0], vec![0, 0, 0]);
/// assert_eq!(codes[1], vec![1, 0, 0]);
/// assert_eq!(codes[2], vec![1, 1, 0]);
/// ```
pub fn brgc(n: u32) -> impl Iterator<Item = Vec<u8>> {
    Brgc::new(n)
}

struct Brgc {
    lst: Vec<u8>,
    flips: Box<dyn Iterator<Item = u32>>,
    yielded_initial: bool,
}

impl Brgc {
    fn new(n: u32) -> Self {
        Self {
            lst: vec![0; n as usize],
            flips: Box::new(brgc_gen(n)),
            yielded_initial: false,
        }
    }
}

impl Iterator for Brgc {
    type Item = Vec<u8>;
    
    fn next(&mut self) -> Option<Self::Item> {
        if !self.yielded_initial {
            self.yielded_initial = true;
            return Some(self.lst.clone());
        }
        
        if let Some(i) = self.flips.next() {
            self.lst[i as usize] = 1 - self.lst[i as usize]; // flip
            Some(self.lst.clone())
        } else {
            None
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_brgc_gen() {
        let flips: Vec<u32> = brgc_gen(4).collect();
        let expected = vec![0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1, 0];
        assert_eq!(flips, expected);
    }
    
    #[test]
    fn test_brgc_gen_1() {
        let flips: Vec<u32> = brgc_gen(1).collect();
        assert_eq!(flips, vec![0]);
    }
    
    #[test]
    fn test_brgc_gen_2() {
        let flips: Vec<u32> = brgc_gen(2).collect();
        assert_eq!(flips, vec![0, 1, 0]);
    }
    
    #[test]
    fn test_brgc() {
        let codes: Vec<Vec<u8>> = brgc(3).collect();
        assert_eq!(codes.len(), 8); // 2^3 = 8 codes
        
        // Check first few codes
        assert_eq!(codes[0], vec![0, 0, 0]);
        assert_eq!(codes[1], vec![1, 0, 0]);
        assert_eq!(codes[2], vec![1, 1, 0]);
        assert_eq!(codes[3], vec![0, 1, 0]);
        
        // Verify Gray code property: consecutive codes differ by exactly one bit
        for i in 0..codes.len() - 1 {
            let diff_count = codes[i]
                .iter()
                .zip(codes[i + 1].iter())
                .filter(|(a, b)| a != b)
                .count();
            assert_eq!(diff_count, 1, "Codes at positions {} and {} differ by {} bits", i, i + 1, diff_count);
        }
    }
    
    #[test]
    fn test_brgc_4() {
        let codes: Vec<Vec<u8>> = brgc(4).collect();
        assert_eq!(codes.len(), 16); // 2^4 = 16 codes
        
        // Verify all codes are unique
        let mut sorted = codes.clone();
        sorted.sort();
        sorted.dedup();
        assert_eq!(sorted.len(), codes.len());
    }
}