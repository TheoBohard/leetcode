# Two Sum - Optimized Approach

## Problem

Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers such that they add up to `target`.

---

## Idea

We use a **hash map (dictionary)** to store numbers we have seen so far along with their indices.  
For each number in the array, we calculate its **complement** (i.e., `target - number`) and check if this complement already exists in the hash map:

- If the complement exists, we have found the two numbers and return their indices.
- If not, we add the current number and its index to the hash map and continue.

This approach ensures we find the solution in **one pass** through the array with **O(n)** time complexity.

---

## Complexity

- **Time Complexity**: O(n)
- **Space Complexity**: O(n)

---
