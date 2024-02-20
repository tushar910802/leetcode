class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Finds the missing number in the given list of integers.

        Parameters:
        - nums (List[int]): The list of integers containing all numbers in the range [0, len(nums)] except one.

        Returns:
        - int: The missing number.
        """
        ans = len(nums)

        for i, num in enumerate(nums):
            ans ^= i ^ num

        return ans