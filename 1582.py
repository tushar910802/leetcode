class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        """
        Counts the number of special positions in a binary matrix where the value at the position is 1 and 
        it's the only one in its row and column.

        Args:
        - mat (List[List[int]]): A binary matrix represented as a list of lists.

        Returns:
        - int: The count of special positions in the matrix.
        """
        m = len(mat)
        n = len(mat[0])
        ans = 0
        rowOnes = [0] * m
        colOnes = [0] * n

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    rowOnes[i] += 1
                    colOnes[j] += 1

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and rowOnes[i] == 1 and colOnes[j] == 1:
                    ans += 1

        return ans