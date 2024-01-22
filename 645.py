class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        Finds the repeating and missing numbers in a given list of integers
        representing values from 1 to n.

        Parameters:
        - nums (List[int]): A list of integers containing values from 1 to n, where n
          is the length of the list.

        Returns:
        - List[int]: A list containing two elements - the repeating number and the
          missing number.

        Example:
        findErrorNums([1, 2, 2, 4]) should return [2, 3], as 2 is the repeating number,
        and 3 is the missing number.

        Note:
        - The function uses negation to mark visited numbers and identify the repeating
          number.
        - The missing number is determined by finding the non-negated index.

        Complexity:
        - Time: O(N), where N is the length of the input list.
        - Space: O(1), as the function uses constant space for variables.
        """
        
        
        for num in nums:
            if nums[abs(num) - 1] < 0:
                duplicate = abs(num)
            else:
                nums[abs(num) - 1] *= -1

        for i, num in enumerate(nums):
            if num > 0:
                return [duplicate, i + 1]