class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "AEIOUaeiou"

        count = {v: 0 for v in vowels}

        for char in s:
            if char in count:
                count[char] += 1

        sorted_vowels = []
        for v in vowels:
            sorted_vowels.extend([v] * count[v])

        result = []
        vowel_index = 0

        for char in s:
            if char in count:
                result.append(sorted_vowels[vowel_index])
                vowel_index += 1
            else:
                result.append(char)

        return "".join(result)
