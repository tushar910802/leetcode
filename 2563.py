class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        """
        Given a list of integers `nums` and two integers `lower` and `upper`, 
        this function counts the number of pairs (i, j) such that:
        - i < j
        - lower <= nums[i] + nums[j] <= upper
        
        Parameters:
        nums (List[int]): The list of integers in which we need to find the fair pairs.
        lower (int): The lower bound for the sum of each pair.
        upper (int): The upper bound for the sum of each pair.
        
        Returns:
        int: The number of fair pairs (i, j) that satisfy the given conditions.
        """
        
        # Sort the array to use two-pointer technique for efficient counting
        nums.sort()

        def countLess(summ: int) -> int:
            """
            Helper function to count how many pairs (i, j) in the sorted list 
            satisfy nums[i] + nums[j] <= summ.
            
            Parameters:
            summ (int): The sum threshold.
            
            Returns:
            int: The number of valid pairs (i, j) where nums[i] + nums[j] <= summ.
            """
            res = 0  # Variable to store the count of valid pairs
            i = 0  # Left pointer
            j = len(nums) - 1  # Right pointer

            # Use two-pointer approach to count pairs
            while i < j:
                # If the sum of nums[i] and nums[j] exceeds the threshold, move the right pointer left
                while i < j and nums[i] + nums[j] > summ:
                    j -= 1
                # Count all pairs with nums[i] where i < j and the sum is <= summ
                res += j - i
                # Move the left pointer right to check for new pairs
                i += 1
            
            return res

        # Count pairs where the sum is within [lower, upper]
        return countLess(upper) - countLess(lower - 1)