class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        """
        Calculates the difference between counts of ones and zeros in rows and columns of a grid.

        Args:
        - grid (List[List[int]]): A 2D grid consisting of 0s and 1s.

        Returns:
        - List[List[int]]: A 2D grid where each cell represents the count of ones minus the count of zeros
                        in the corresponding row and column of the input grid.
        """
        m = len(grid)
        n = len(grid[0])
        ans = [[0] * n for _ in range(m)]
        onesRow = [row.count(1) for row in grid]
        onesCol = [col.count(1) for col in zip(*grid)]

        for i in range(m):
            for j in range(n):
                ans[i][j] = onesRow[i] + onesCol[j] - \
                    (n - onesRow[i]) - (m - onesCol[j])

        return ans