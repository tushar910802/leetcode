class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        """
        Finds the maximum length of a subarray that contains at most k distinct elements.

        Parameters:
        - nums (List[int]): The input array of integers.
        - k (int): The maximum number of distinct elements allowed in the subarray.

        Returns:
        - int: The maximum length of a subarray with at most k distinct elements.

        Example:
        maxSubarrayLength([1, 2, 1, 2, 3], 2) should return 4, as the subarray [1, 2, 1, 2]
        contains at most 2 distinct elements.

        Note:
        - The function uses a sliding window approach to find the maximum length subarray.
        - It maintains a count of the occurrences of each element in the current window.
        - The result is the maximum length of a subarray with at most k distinct elements.
        """
        ans = 0
        count = collections.Counter()

        l = 0
        for r, num in enumerate(nums):
            count[num] += 1
            while count[num] == k + 1:
                count[nums[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)

        return ans