class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        """
        Counts the number of negative numbers in a 2D grid.

        Args:
            grid: A 2D list of integers.

        Returns:
            The number of negative numbers in the grid.
        """

        m = len(grid)
        n = len(grid[0])
        ans = 0
        i = m - 1
        j = 0

        while i >= 0 and j < n:
            if grid[i][j] < 0:
                ans += n - j
                i -= 1
            else:
                j += 1

        return ans


## 1351. Count Negative Numbers in a Sorted Matrix