# Sort Vowels in a String - Optimized Approach

## Problem

Given a 0-indexed string `s`, permute `s` to get a new string `t` such that:

- All consonants remain in their original places. More formally, if there is an index `i` with `0 <= i < s.length` such that `s[i]` is a consonant, then `t[i] = s[i]`.
- The vowels must be sorted in the nondecreasing order of their ASCII values. More formally, for pairs of indices `i`, `j` with `0 <= i < j < s.length` such that `s[i]` and `s[j]` are vowels, then `t[i]` must not have a higher ASCII value than `t[j]`.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in lowercase or uppercase. Consonants comprise all letters that are not vowels.

## Idea

1. **Count the Vowels**: We first count the occurrences of each vowel in the input string `s`. This can be efficiently done using a regular dictionary where the vowels are keys, and their counts are the values.

2. **Sort the Vowels**: Using a predefined order of vowels (`"AEIOUaeiou"`), we generate a list of vowels sorted in ascending order. This step is achieved by repeating each vowel according to its count.

3. **Rebuild the String**: After sorting the vowels, we iterate over the original string. If a character is a vowel, we replace it with the next vowel from the sorted list, otherwise, we keep the consonant in its original position.

## Complexity

- **Time Complexity**: 
  - **O(n)** for counting the vowels and rebuilding the string, where `n` is the length of the string.
  - Sorting the vowels is avoided by leveraging the fixed order of vowels (`"AEIOUaeiou"`), making this part an **O(1)** operation.

- **Space Complexity**: 
  - **O(n)** due to the space needed for the `sorted_vowels` and `result` lists, both of which may hold up to `n` elements in the worst case.
  - The space used by the dictionary for counting vowels is **O(1)** since there are only 10 distinct vowels.
