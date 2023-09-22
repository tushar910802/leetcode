class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, return whether or not s is a subsequence of t.

        A subsequence of a string is a new string formed from the original string by deleting some (or no) of the characters without changing the relative order of the remaining characters. For example, "ace" is a subsequence of "abcde".

        Args:
            s: str
            t: str

        Returns:
            bool
        """
        if not s:
            return True
        
        i = 0
        for c in t:
            if c == s[i]:
                i += 1
            if i >= len(s):
                break
                
        if i == len(s):     
            return True
        return False


## 392. Is Subsequence
