class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        """
        Computes the moving averages of a list of numbers.

        Args:
            nums: A list of numbers.
            k: The window size for the moving averages.

        Returns:
            A list of moving averages.
        """
        n = len(nums)
        size = 2 * k + 1
        ans = [-1] * n
        if size > n:
            return ans

        summ = sum(nums[:size])

        for i in range(k, n - k):
            ans[i] = summ // size
            if i + k + 1 < n:
                summ += nums[i + k + 1] - nums[i - k]

        return ans

## 2090. K Radius Subarray Averages