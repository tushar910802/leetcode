class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        """
        This function determines whether Player 1 can win the game of Predict the Winner.

        Args:
            nums: A list of integers representing the numbers in the game.

        Returns:
            True if Player 1 can win, False otherwise.

        """
        n = len(nums)
        dp = nums[:]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])

        return dp[-1] >= 0


## 486. Predict the Winner