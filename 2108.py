class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        """
        Finds the first palindrome in the given list of words.

        Parameters:
        - words (List[str]): The list of words.

        Returns:
        - str: The first palindrome found, or an empty string if none found.
        """
        def isPalindrome(s: str) -> bool:
            i = 0
            j = len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        return next((word for word in words if isPalindrome(word)), '')