#pragma once

/**
 * @file ecgen.hpp
 * @brief Main header for the Enumerative Combinatoric Generation library
 * @version 0.1.0
 * @date 2025-12-16
 * 
 * @copyright Copyright (c) 2025
 * 
 * This library provides C++23 implementations of combinatorial generation algorithms
 * including combinations, permutations, set partitions, Gray codes, and more.
 */

#include "combin.hpp"
#include "set_partition.hpp"
#include "sjt.hpp"
#include "gray_code.hpp"
#include "ehr.hpp"
#include "set_bipart.hpp"
#include "skeleton.hpp"

namespace ecgen {

    /**
     * @brief Library version information
     */
    struct version_info {
        static constexpr int major = 0;
        static constexpr int minor = 1;
        static constexpr int patch = 0;
        static constexpr const char* string = "0.1.0";
    };

} // namespace ecgen