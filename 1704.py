class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        """
        Checks if the first and second halves of a given string have the same number
        of vowels (case-insensitive).

        Parameters:
        - s (str): The input string to be checked.

        Returns:
        - bool: True if the number of vowels in the first half is equal to the number
                of vowels in the second half, False otherwise.

        Example:
        halvesAreAlike("abcdeABCDE") should return True, as both halves "abcde" and "ABCDE"
        contain the same number of vowels (2).

        Note:
        - Vowels are considered to be 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'.
        - The input string can have even or odd length.

        Complexity:
        - Time: O(N), where N is the length of the input string.
        - Space: O(1), as we use a constant amount of space for the vowel set and
                variables to count the number of vowels.
        """
        s1 =  "aeiouAEIOU"
        
        count_i1 = 0
        count_i2 = 0
        l = int(len(s)/2)
        for i in range(0,l):
            if s[i] in s1:
                count_i1 += 1
            if s[i + l] in s1:
                count_i2 += 1
        return count_i1 == count_i2