//! Basic example demonstrating the use of combinatorial generation algorithms.

use rust_ai::combin::emk;
use rust_ai::ehr::ehr_gen;
use rust_ai::gray_code::brgc;
use rust_ai::sjt::sjt_gen;
use rust_ai::skeleton::fib;

fn main() {
    println!("=== Fibonacci Example ===");
    println!("fib(10) = {}", fib(10));
    println!();

    println!("=== Combinations (EMK algorithm) ===");
    println!("All combinations of 6 choose 3:");
    for (idx, combination) in emk(6, 3, 0, 1).enumerate() {
        println!("  {}: {:?}", idx + 1, combination);
    }
    println!();

    println!("=== Gray Codes ===");
    println!("Binary Reflected Gray Code for 3 bits:");
    for (idx, code) in brgc(3).enumerate() {
        println!("  {}: {:?}", idx + 1, code);
    }
    println!();

    println!("=== Permutations (EHR algorithm) ===");
    println!("Generating permutations of 4 elements:");
    let mut perm = vec![0, 1, 2, 3];
    println!("  Start: {:?}", perm);
    for (idx, swap_idx) in ehr_gen(4).enumerate() {
        perm.swap(0, swap_idx as usize);
        println!("  {}: swap 0 with {} -> {:?}", idx + 1, swap_idx, perm);
    }
    println!();

    println!("=== Permutations (SJT algorithm) ===");
    println!("Generating permutations of 3 elements with adjacent swaps:");
    let mut perm = vec!["A", "B", "C"];
    println!("  Start: {:?}", perm);
    for (idx, swap_idx) in sjt_gen(3).enumerate() {
        perm.swap(swap_idx as usize, swap_idx as usize + 1);
        println!(
            "  {}: swap {} with {} -> {:?}",
            idx + 1,
            swap_idx,
            swap_idx + 1,
            perm
        );
    }
}
