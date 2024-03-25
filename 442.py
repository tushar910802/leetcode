class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        Finds all the duplicates in an array of integers.

        Parameters:
        - nums (List[int]): The input array of integers.

        Returns:
        - List[int]: A list of duplicate integers in the input array.

        Example:
        findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]) should return [2, 3], as these are
        the duplicate integers in the input array.

        Note:
        - The function uses negation to mark visited numbers.
        - It iterates through the array and marks each visited number by negating
          the value at its corresponding index (using abs(num) - 1).
        - If a number is already marked as negative, it means the number is a duplicate,
          and it is added to the result list.
        - The result is a list of duplicate integers in the input array.
        """
        ans = []

        for num in nums:
            nums[abs(num) - 1] *= -1
            if nums[abs(num) - 1] > 0:
                ans.append(abs(num))

        return ans