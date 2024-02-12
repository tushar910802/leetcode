class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Finds the majority element in the given list of integers.

        Parameters:
        - nums (List[int]): The list of integers.

        Returns:
        - int: The majority element.
        """
        counter = {}
        
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        return max(counter.keys(), key=counter.get)