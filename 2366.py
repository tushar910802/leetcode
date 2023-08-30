class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        """
        Calculates the minimum number of replacements needed to make all the elements in the list equal to the largest element.

        Args:
            nums: The list of integers.

        Returns:
            The minimum number of replacements.

        """
        ans = 0

        max = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            ops = (nums[i] - 1) // max
            ans += ops
            max = nums[i] // (ops + 1)

        return ans

## 2366. Minimum Replacements to Sort the Array
