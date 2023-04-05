class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        """
        Given an integer list `nums`, returns the maximum possible average of any contiguous subarray of `nums` after
        minimizing the values of the array. Minimizing the array means that you can subtract a value `k` from any element
        of the array, but you can't subtract different values from different elements.

        Args:
            nums: A list of integers.

        Returns:
            The maximum possible average of any contiguous subarray of `nums` after minimizing the values of the array.

        Example:
            >>> minimizeArrayValue([4, 2, 3, 1, 5])
            2
        """
        ans = 0
        prefix = 0

        for i, num in enumerate(nums):
            prefix += num
            prefixAvg = math.ceil(prefix / (i + 1))
            ans = max(ans, prefixAvg)

        return ans

## 2439. Minimize Maximum of Array