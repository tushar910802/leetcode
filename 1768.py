class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Merges two strings alternately, returning the merged string.

        Args:
        - word1 (str): The first string to be merged.
        - word2 (str): The second string to be merged.

        Returns:
        - str: The merged string containing the characters from word1 and word2 alternately.

        Example:
        mergeAlternately('abc', 'defg') returns 'adbecfg'.
        """
        return ''.join(a + b for a, b in zip_longest(word1, word2, fillvalue=''))

## 1768. Merge Strings Alternately
