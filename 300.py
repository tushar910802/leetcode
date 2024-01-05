class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Finds the length of the longest increasing subsequence (LIS) in the given list of integers.

        Args:
        - nums (List[int]): A list of integers.

        Returns:
        - int: The length of the longest increasing subsequence.

        Algorithm:
        1. Initialize a dynamic programming list 'dp' with length equal to 'nums', filled with 1s.
        2. Iterate through 'nums':
            - For each element 'nums[i]', iterate through the elements before it ('nums[j]') where j < i.
            - If 'nums[j]' is less than 'nums[i]', update dp[i] as max(dp[i], dp[j] + 1).
        3. Return the maximum value present in the 'dp' list, which represents the length of the LIS.

        Example:
        Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) returns 4
        - Explanation: The longest increasing subsequence is [2, 3, 7, 101], hence the length is 4.
        """
        if not nums:
            return 0
        
        dp = [1] * len(nums)
        
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    
        return max(dp)