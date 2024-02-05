class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        Finds the index of the first unique character in the given string.

        Parameters:
        - s (str): The input string.

        Returns:
        - int: The index of the first unique character, or -1 if none found.
        """
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        
        for i, ch in enumerate(s):
            if count[ch] == 1:
                return i
        
        return -1
