class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        Counts the number of contiguous subarrays where the product of all elements
        is less than a given value 'k'.

        Parameters:
        - nums (List[int]): The input array of integers.
        - k (int): The target product value.

        Returns:
        - int: The number of contiguous subarrays where the product is less than 'k'.

        Example:
        numSubarrayProductLessThanK([10, 5, 2, 6], 100) should return 8, as there are
        8 subarrays with a product less than 100: [10], [5], [2], [6], [10, 5], [5, 2],
        [2, 6], [5, 2, 6].

        Note:
        - The function uses a sliding window approach to count the subarrays.
        - It maintains a window where the product of all elements is less than 'k'.
        - The result is the sum of the lengths of all valid subarrays.
        """
        if k <= 1:
            return 0

        ans = 0
        prod = 1

        j = 0
        for i, num in enumerate(nums):
            prod *= num
            while prod >= k:
                prod /= nums[j]
                j += 1
            ans += i - j + 1

        return ans