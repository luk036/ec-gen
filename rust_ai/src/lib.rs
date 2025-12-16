//! Rust AI - Combinatorial Generation Algorithms
//!
//! This library provides Rust implementations of combinatorial generation algorithms
//! using `genawaiter` for async/await-style generators.
//!
//! # Algorithms
//!
//! - **Combinations Generator** (`combin.rs`) - EMK algorithm for generating combinations
//! - **Ehrlich-Hopcroft-Reingold Algorithm** (`ehr.rs`) - Permutation generation
//! - **Binary Reflected Gray Code** (`gray_code.rs`) - Gray code generation
//! - **Set Bipartition** (`set_bipart.rs`) - Set bipartition generation
//! - **Set Partition** (`set_partition.rs`) - Set partition generation
//! - **Steinhaus-Johnson-Trotter Algorithm** (`sjt.rs`) - Permutation generation
//! - **Skeleton** (`skeleton.rs`) - Example and utility functions
//!
//! # Examples
//!
//! ```
//! use rust_ai::combin::emk;
//!
//! for combination in emk(6, 3, 0, 1) {
//!     println!("{:?}", combination);
//! }
//! ```

pub mod combin;
pub mod ehr;
pub mod gray_code;
pub mod set_bipart;
pub mod set_partition;
pub mod sjt;
pub mod skeleton;
