class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Calculates the maximum amount of money that can be robbed from a row of houses,
        where adjacent houses cannot be robbed.

        Parameters:
        - nums (List[int]): A list representing the amount of money in each house.

        Returns:
        - int: The maximum amount of money that can be robbed.

        Example:
        rob([2, 7, 9, 3, 1]) should return 12, as the optimal strategy is to rob
        houses 1, 3, and 5, yielding a total of 2 + 9 + 1 = 12.

        Note:
        - The function uses dynamic programming to calculate the maximum amount of
          money that can be robbed.
        - It maintains an array 'f' where f[i] represents the maximum amount of money
          that can be robbed up to the ith house.
        - The final result is stored in f[n-1], where n is the number of houses.

        Complexity:
        - Time: O(N), where N is the number of houses.
        - Space: O(N), as the function uses an array of size N for dynamic programming.
        """
        if nums == None or len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)
        f = [0 for i in range(0,n)]
        
        f[0] = nums[0]
        f[1] = max(f[0],nums[1])
        
        for i in range(2,n):
            f[i] = max(f[i-1],f[i-2] + nums[i])
        
        return f[n-1]