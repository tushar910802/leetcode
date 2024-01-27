class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        """
        Calculates the number of permutations of numbers 1 to n with k inverse pairs.

        Parameters:
        - n (int): The total number of elements in the permutation.
        - k (int): The desired number of inverse pairs.

        Returns:
        - int: The number of permutations with k inverse pairs.

        Example:
        kInversePairs(3, 1) should return 2, as there are two permutations with
        1 inverse pair: [1, 3, 2] and [2, 1, 3].

        Note:
        - The function uses dynamic programming to calculate the number of permutations
          with a given number of inverse pairs.
        - It builds a 2D array 'dp' where dp[i][j] represents the number of
          permutations of numbers 1..i with j inverse pairs.
        - The result is stored in dp[n][k].

        Complexity:
        - Time: O(n*k), where n is the total number of elements and k is the desired
          number of inverse pairs.
        - Space: O(n*k), as the function uses a 2D array of size (n+1) x (k+1) for
          dynamic programming.
        """
        kMod = 1_000_000_007
        # dp[i][j] := the number of permutations of numbers 1..i with j inverse pairs
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        # If there's no inverse pair, the permutation is unique '123..i'
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % kMod
                if j - i >= 0:
                    dp[i][j] = (dp[i][j] - dp[i - 1][j - i] + kMod) % kMod

        return dp[n][k]