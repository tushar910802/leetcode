class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Finds the first missing positive integer in an array of integers.

        Parameters:
        - nums (List[int]): The input array of integers.

        Returns:
        - int: The first missing positive integer in the input array.

        Example:
        firstMissingPositive([1, 2, 0]) should return 3, as the first missing positive
        integer in the array [1, 2, 0] is 3.

        Note:
        - The function reorganizes the array such that nums[i] = i + 1 for each valid index i.
        - It then iterates through the array and returns the first index i where nums[i] != i + 1,
          indicating the first missing positive integer.
        - If no missing positive integer is found, the function returns n + 1, where n is the length
          of the input array.
        """
        n = len(nums)

        # Correct slot:
        # nums[i] = i + 1
        # nums[i] - 1 = i
        # nums[nums[i] - 1] = nums[i]
        for i in range(n):
            while nums[i] > 0 and nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i, num in enumerate(nums):
            if num != i + 1:
                return i + 1

        return n + 1