class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """
        Returns the minimum ASCII delete sum for two strings.

        Args:
            s1: The first string.
            s2: The second string.

        Returns:
            The minimum ASCII delete sum for the two strings.
        """
        dp = [[0] * (len(s2)+1) for _ in range(2)]
        for j in range(len(s2)):
            dp[0][j+1] = dp[0][j] + ord(s2[j])

        for i in range(len(s1)):
            dp[(i+1)%2][0] = dp[i%2][0] + ord(s1[i])
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    dp[(i+1)%2][j+1] = dp[i%2][j]
                else:
                    dp[(i+1)%2][j+1] = min(dp[i%2][j+1] + ord(s1[i]), \
                                           dp[(i+1)%2][j] + ord(s2[j]))

        return dp[len(s1)%2][-1]

## 712. Minimum ASCII Delete Sum for Two Strings
