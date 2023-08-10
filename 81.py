class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        Searches for the given target in the sorted array nums.

        Args:
            nums: The sorted array to search in.
            target: The target value to search for.

        Returns:
            True if the target is found in the array, False otherwise.

        Raises:
            ValueError: If the array is empty.
        """
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return True
            if nums[l] == nums[m] == nums[r]:
                l += 1
                r -= 1
            elif nums[l] <= nums[m]:  # nums[l..m] are sorted
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:  # nums[m..n - 1] are sorted
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return False

## 81. Search in Rotated Sorted Array II