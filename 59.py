class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        Given an integer n, generates a square matrix of size n x n, filled with
        numbers from 1 to n^2 in spiral order, starting from the top left corner.

        Args:
        - n: An integer representing the size of the square matrix.

        Returns:
        - A list of n lists, each containing n integers, representing the generated
        square matrix filled with numbers in spiral order.
        """
        ans = [[0] * n for _ in range(n)]
        count = 1

        for min in range(n // 2):
            max = n - min - 1
            for i in range(min, max):
                ans[min][i] = count
                count += 1
            for i in range(min, max):
                ans[i][max] = count
                count += 1
            for i in range(max, min, -1):
                ans[max][i] = count
                count += 1
            for i in range(max, min, -1):
                ans[i][min] = count
                count += 1

        if n & 1:
            ans[n // 2][n // 2] = count

        return ans

## 59. Spiral Matrix II
