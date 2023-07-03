class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        """
        This function checks if two strings are buddy strings.

        A buddy string is a string where two of the characters can be swapped to make the string equal to another string.

        Parameters
        ----------
        A : str
            The first string to check.
        B : str
            The second string to check.

        Returns
        -------
        bool
            True if the two strings are buddy strings, False otherwise.
        """
        if len(A) != len(B):
            return False
        if A == B and len(set(A)) < len(A):
            return True

        diff = [(a, b) for a, b in zip(A, B) if a != b]

        return len(diff) == 2 and diff[0] == diff[1][::-1]

## 859. Buddy Strings
