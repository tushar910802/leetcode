class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Calculates the minimum cost to reach the top of a staircase with the given costs.

        Args:
            cost: A list of integers, where `cost[i]` is the cost of climbing the `i`th step.

        Returns:
            The minimum cost to reach the top of the staircase.
        """
        N = len(cost)
        dp = [0]*N
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2,N):
            dp[i] = cost[i] + min(dp[i-1],dp[i-2])
            
        return min(dp[-2:])
## 746. Min Cost Climbing Stairs
