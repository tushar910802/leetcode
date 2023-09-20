class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        """Returns the minimum number of operations needed to reduce the sum of the
        given list of numbers `nums` to `x`.

        An operation consists of either:

        * Removing a single number from the list, or
        * Reversing the order of the list.

        If it is impossible to reduce the sum of the list to `x`, the function
        returns `-1`.

        Args:
            nums: A list of integers.
            x: The target sum.

        Returns:
            The minimum number of operations needed to reduce the sum of the list to `x`,
            or `-1` if it is impossible.
        """
        x = sum(nums) - x
        vis = {0: -1}
        ans = inf
        s, n = 0, len(nums)
        for i, v in enumerate(nums):
            s += v
            if s not in vis:
                vis[s] = i
            if s - x in vis:
                j = vis[s - x]
                ans = min(ans, n - (i - j))
        return -1 if ans == inf else ans
        


## 1658. Minimum Operations to Reduce X to Zero
