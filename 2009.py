class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        Finds the minimum number of operations to reduce the given list of numbers to zero.

        Args:
            nums: A list of positive integers.

        Returns:
            The minimum number of operations required to reduce the given list of numbers
            to zero.

        Example:

            >>> minOperations([1, 2, 3, 4])
            3
        """
        n = len(nums)
        ans = n
        nums = sorted(set(nums))

        for i, start in enumerate(nums):
            end = start + n - 1
            index = bisect_right(nums, end)
            uniqueLength = index - i
            ans = min(ans, n - uniqueLength)

        return ans