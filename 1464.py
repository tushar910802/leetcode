class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Finds the maximum product of two distinct elements in the given list of integers.

        Args:
        - nums (List[int]): A list of integers.

        Returns:
        - int: The maximum product of two distinct elements in the list.
        """
        max1 = 0
        max2 = 0

        for num in nums:
            if num > max1:
                max2, max1 = max1, num
            elif num > max2:
                max2 = num

        return (max1 - 1) * (max2 - 1)