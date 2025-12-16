//! Basic example of using the ec-gen Rust library

use rust_ai::combin::comb;
use rust_ai::gray_code::brgc;
use rust_ai::skeleton::fib;

fn main() {
    println!("=== Basic Examples ===\n");
    
    // Combinations
    println!("Combinations C(6,3) = {}", comb(6, 3));
    println!("Combinations C(5,2) = {}", comb(5, 2));
    
    // Fibonacci
    println!("\nFibonacci numbers:");
    for i in 1..=10 {
        println!("  fib({}) = {}", i, fib(i));
    }
    
    // Gray codes for n=3
    println!("\nGray codes for n=3:");
    for (i, code) in brgc(3).enumerate() {
        println!("  {}: {:?}", i, code);
    }
    
    println!("\n=== Done ===");
}