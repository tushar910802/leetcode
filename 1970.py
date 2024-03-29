class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        """
        Given an m x n grid of cells, each cell has an initial value of 0.

        Each day, a cell with value 0 becomes 1 if it is adjacent to at least one cell that has value 1.

        Find the latest day where you can still walk from the leftmost cell to the rightmost cell.

        Note that you can only walk on cells with value 1.

        Args:
            row: The number of rows in the grid.
            col: The number of columns in the grid.
            cells: A list of lists of integers representing the initial values of the cells.

        Returns:
            The latest day where you can still walk from the leftmost cell to the rightmost cell.
        """

        dirs = [0, 1, 0, -1, 0]

        def canWalk(day: int) -> bool:
            matrix = [[0] * col for _ in range(row)]
            for i in range(day):
                x, y = cells[i]
                matrix[x - 1][y - 1] = 1

            q = collections.deque()

            for j in range(col):
                if matrix[0][j] == 0:
                    q.append((0, j))
                    matrix[0][j] = 1

            while q:
                i, j = q.popleft()
                for k in range(4):
                    x = i + dirs[k]
                    y = j + dirs[k + 1]
                    if x < 0 or x == row or y < 0 or y == col:
                        continue
                    if matrix[x][y] == 1:
                        continue
                    if x == row - 1:
                        return True
                    q.append((x, y))
                    matrix[x][y] = 1

            return False

        ans = 0
        l = 1
        r = len(cells) - 1

        while l <= r:
            m = (l + r) // 2
            if canWalk(m):
                ans = m
                l = m + 1
            else:
                r = m - 1

        return ans

## 1970. Last Day Where You Can Still Cross