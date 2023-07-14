class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        """
    This function finds the longest subsequence in the given array where the difference between adjacent elements is equal to `difference`.

    Args:
        arr: The input array.
        difference: The difference between adjacent elements in the subsequence.

    Returns:
        The length of the longest subsequence.
    """
        ans = 0
        lengthAt = {}

        for a in arr:
            lengthAt[a] = lengthAt.get(a - difference, 0) + 1
            ans = max(ans, lengthAt[a])

        return ans

## 1218. Longest Arithmetic Subsequence of Given Difference