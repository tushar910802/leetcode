class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Returns the elements of the input matrix in diagonal order.

        Traverses the matrix diagonally and returns its elements in a list, following
        a pattern from the top-right to bottom-left within the same diagonal line.

        Args:
        - matrix (List[List[int]]): A 2D matrix of integers.

        Returns:
        - List[int]: The elements of the matrix in diagonal order.
        """
        diagonal_elements = []
      
        # Iterate through the matrix rows
        for row_index, row in enumerate(matrix):
            # Iterate through the elements in the current row
            for column_index, value in enumerate(row):
                # The sum of row and column indices gives the diagonal index.
                # Append a tuple containing the diagonal index, column index and the value
                diagonal_elements.append((row_index + column_index, column_index, value))
      
        # Sort the list of tuples based on diagonal index, then by column index (as secondary)
        # This will order the elements first by diagonal, then from top-right to bottom-left
        # within the same diagonal line.
        diagonal_elements.sort()
      
        # Extract the values from the sorted list of tuples and return them in the correct order
        return [element[2] for element in diagonal_elements]