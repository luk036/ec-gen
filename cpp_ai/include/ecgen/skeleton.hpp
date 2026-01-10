#pragma once

#include <cppcoro/generator.hpp>
#include <cstdint>
#include <vector>
#include <concepts>
#include <ranges>

namespace ecgen {

    /**
     * @brief Skeleton algorithm for combinatorial generation
     *
     * Provides a framework for generating combinatorial objects
     * using a skeleton structure that can be specialized for
     * different types of objects.
     */

    /**
     * @brief Base skeleton generator interface
     *
     * @tparam T Type of combinatorial object
     */
    template<typename T>
    class skeleton_generator {
    public:
        virtual ~skeleton_generator() = default;

        /**
         * @brief Generate next object
         *
         * @return Generated object, or empty optional if done
         */
        virtual auto next() -> cppcoro::generator<T> = 0;

        /**
         * @brief Reset generator to initial state
         */
        virtual void reset() = 0;

        /**
         * @brief Check if generation is complete
         */
        virtual bool done() const = 0;
    };

    /**
     * @brief Generic combinatorial skeleton
     *
     * Implements the skeleton algorithm for generating
     * combinatorial objects using a visit/backtrack pattern.
     */
    template<typename T>
    class combinatorial_skeleton {
    public:
        using object_type = T;
        using visitor_type = std::function<bool(const T&)>;

        combinatorial_skeleton() = default;

        /**
         * @brief Generate all objects
         *
         * @param visitor Function called for each generated object
         * @return true if all objects generated successfully
         */
        auto generate(visitor_type visitor) -> cppcoro::generator<bool> {
            T current = initial_object();
            co_yield backtrack(current, 0, visitor);
        }

    protected:
        /**
         * @brief Create initial object
         */
        virtual auto initial_object() -> T = 0;

        /**
         * @brief Backtracking algorithm
         */
        virtual auto backtrack(T& current, int depth, visitor_type visitor) -> bool {
            if (is_complete(current, depth)) {
                if (!visitor(current)) {
                    co_yield false;
                }
                co_yield true;
            }

            auto candidates = generate_candidates(current, depth);
            for (auto& candidate : candidates) {
                if (is_valid(candidate, current, depth)) {
                    make_move(current, candidate, depth);
                    if (!backtrack(current, depth + 1, visitor)) {
                        co_yield false;
                    }
                    undo_move(current, candidate, depth);
                }
            }

            co_yield true;
        }

        /**
         * @brief Check if object is complete
         */
        virtual bool is_complete(const T& obj, int depth) const = 0;

        /**
         * @brief Generate candidate moves
         */
        virtual auto generate_candidates(const T& obj, int depth) -> std::vector<T> = 0;

        /**
         * @brief Check if candidate is valid
         */
        virtual bool is_valid(const T& candidate, const T& current, int depth) const = 0;

        /**
         * @brief Apply move
         */
        virtual void make_move(T& current, const T& candidate, int depth) = 0;

        /**
         * @brief Undo move
         */
        virtual void undo_move(T& current, const T& candidate, int depth) = 0;
    };

    /**
     * @brief Example: Skeleton for permutation generation
     */
    class permutation_skeleton : public combinatorial_skeleton<std::vector<int>> {
    public:
        permutation_skeleton(int n) : n_(n) {}

    protected:
        auto initial_object() -> std::vector<int> override {
            std::vector<int> perm(n_);
            for (int i = 0; i < n_; ++i) {
                perm[i] = i + 1;
            }
            return perm;
        }

        bool is_complete(const std::vector<int>& perm, int depth) const override {
            return depth == n_;
        }

        auto generate_candidates(const std::vector<int>& perm, int depth) -> std::vector<std::vector<int>> override {
            std::vector<std::vector<int>> candidates;
            for (int i = depth; i < n_; ++i) {
                auto candidate = perm;
                std::swap(candidate[depth], candidate[i]);
                candidates.push_back(candidate);
            }
            return candidates;
        }

        bool is_valid(const std::vector<int>& candidate, const std::vector<int>& current, int depth) const override {
            return true; // All swaps are valid for permutations
        }

        void make_move(std::vector<int>& current, const std::vector<int>& candidate, int depth) override {
            // Move already applied in generate_candidates
        }

        void undo_move(std::vector<int>& current, const std::vector<int>& candidate, int depth) override {
            // Would need to track moves to undo
        }

    private:
        int n_;
    };

} // namespace ecgen
