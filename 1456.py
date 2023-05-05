class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """
        This function returns the maximum number of vowels that can be found in a contiguous substring
        of length k within the given input string s.

        Args:
        s (str): The input string.
        k (int): The length of the contiguous substring.

        Returns:
        int: The maximum number of vowels in a contiguous substring of length k.
        """
        max_vowel=0
        res =0
        for i in range(0,len(s)):
            if i>=k :
                if s[i-k] in ['a','e','i','o','u']:
                    res -=1
            if s[i] in['a','e','i','o','u']:
                res+=1
            max_vowel = max(max_vowel,res)
            if max_vowel ==k:
                return max_vowel
        return max_vowel