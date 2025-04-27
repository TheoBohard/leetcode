# Palindrome Number - Optimized Approach

## Problem
Given an integer 'x', return true if x is a palindrome, and false otherwise.

---

## Idea
1. **Edge Cases**:
   - Negative numbers and numbers ending with 0 (except `0`) are **not** palindromes.

2. **Reverse Second Half**:
   - Reverse only the second half of the number, comparing it with the first half to check if they are equal.

3. **Even vs Odd Length**:
   - For even length, both halves should be the same.
   - For odd length, ignore the middle digit.

---

## Complexity
- **Time Complexity**: O(log n), where `n` is the number.
- **Space Complexity**: O(1), since we only use a few extra variables.

---
