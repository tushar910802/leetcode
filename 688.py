class Solution:
    def knightProbability(self, n: int, K: int, r: int, c: int) -> float:
        """
        Calculates the probability that a knight will remain on the chessboard after making K moves, starting from the cell (r, c).

        Args:
            n: The size of the chessboard.
            K: The number of moves.
            r: The row index of the starting cell.
            c: The column index of the starting cell.

        Returns:
            The probability that the knight will remain on the chessboard after K moves.
        """
        dirs = [(1, 2), (2, 1), (2, -1), (1, -2),
            (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

        # dp[i][j] := probability to stand on (i, j)
        dp = [[0] * n for _ in range(n)]
        dp[r][c] = 1

        for _ in range(K):
            newDp = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    for dx, dy in dirs:
                        x = i + dx
                        y = j + dy
                        if 0 <= x < n and 0 <= y < n:
                            newDp[i][j] += dp[x][y]
            dp = newDp

        return sum(map(sum, dp)) / 8**K

## 688. Knight Probability in Chessboard

