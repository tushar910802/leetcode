class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Finds the single number in a list of numbers where every other number appears twice.

        Args:
            nums: A list of integers.

        Returns:
            The single number in the list.
        """
        ones = 0
        twos = 0
        
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        
        return ones

## 137. Single Number II
