class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        This function takes a string 's' as input and returns the length of the longest palindromic subsequence of 's'.
        A palindromic subsequence is a subsequence of a string that is also a palindrome, meaning that it reads the same backwards as forwards.

        The function works by using dynamic programming to build a table of lengths of palindromic subsequences for each subsequence of 's'.
        The table is filled from bottom up, and the result is returned by accessing the value at the top right corner of the table.

        Parameters:
        s (str): The input string for which the longest palindromic subsequence length needs to be computed.

        Returns:
        int: The length of the longest palindromic subsequence of 's'.

        Example Usage:
        solution = Solution()
        s = "bbbab"
        result = solution.longestPalindromeSubseq(s)
        print(result) # Output: 4
        """
        if not s: 
            return 0
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]


## 516. Longest Palindromic Subsequence
