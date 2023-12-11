class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        """
        This function takes a list of integers as input and returns the first duplicate element
        found in the list.

        Args:
            arr: A list of integers.

        Returns:
            The first duplicate element found in the list, or None if no duplicates are found.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        n = len(arr)
        quarter = n // 4

        for i in range(n - quarter):
            if arr[i] == arr[i + quarter]:
                return arr[i]
        