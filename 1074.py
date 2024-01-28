class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        """
        Counts the number of submatrices in the given matrix whose sum equals the target.

        Parameters:
        - matrix (List[List[int]]): A 2D matrix of integers.
        - target (int): The target sum.

        Returns:
        - int: The number of submatrices with a sum equal to the target.

        Example:
        numSubmatrixSumTarget([[0,1,0],[1,1,1],[0,1,0]], 0) should return 4, as there
        are four submatrices with a sum of 0: [[0,1,0],[0,0,0],[0,1,0],[0,0,0]].

        Note:
        - The function uses prefix sum technique to efficiently calculate the sum of
          submatrices.
        - It iterates through columns and uses Counter to keep track of prefix sums.
        - The result is the total count of submatrices with a sum equal to the target.

        Complexity:
        - Time: O(m^2 * n), where m is the number of rows and n is the number of columns
          in the matrix.
        - Space: O(m), as the function uses a Counter to store prefix sums.
        """
        m = len(matrix)
        n = len(matrix[0])
        ans = 0

        # Transfer each row in the matrix to the prefix sum.
        for row in matrix:
            for i in range(1, n):
                row[i] += row[i - 1]

        for baseCol in range(n):
            for j in range(baseCol, n):
                prefixCount = collections.Counter({0: 1})
                summ = 0
                for i in range(m):
                    if baseCol > 0:
                        summ -= matrix[i][baseCol - 1]
                    summ += matrix[i][j]
                    ans += prefixCount[summ - target]
                    prefixCount[summ] += 1

        return ans