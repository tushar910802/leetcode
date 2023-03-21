class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        """
        Counts the number of subarrays in the given list of integers that have a zero-filled sum.

        Args:
            nums: A list of integers.

        Returns:
            An integer representing the number of subarrays that have a zero-filled sum.

        Examples:
            >>> zeroFilledSubarray([1, 0, 2, 0, 3, 0, 0, 4])
            5
            >>> zeroFilledSubarray([0, 1, 2, 3])
            1
            >>> zeroFilledSubarray([1, 2, 3])
            0
        """
        ans = 0
        indexBeforeZero = -1
        for i, num in enumerate(nums):
            if num:
                indexBeforeZero = i
            else:
                ans += i - indexBeforeZero
        return ans

## 2348. Number of Zero-Filled Subarrays
