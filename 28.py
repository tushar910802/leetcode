class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Return the index of the first occurrence of the given 'needle' string in the 'haystack' string.

        Args:
        - haystack (str): The string in which to search for the 'needle' string.
        - needle (str): The string to be searched for in the 'haystack' string.

        Returns:
        - An integer representing the index of the first occurrence of the 'needle' string in the 'haystack' string, if found.
        - Returns -1 if the 'needle' string is not found in the 'haystack' string.
        """
        m = len(haystack)
        n = len(needle)

        for i in range(m - n + 1):
            if haystack[i:i + n] == needle:
                return i

        return -1        

## 28. Find the Index of the First Occurrence in a String