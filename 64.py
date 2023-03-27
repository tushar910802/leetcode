class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Given a grid of non-negative integers, find the path from the top-left corner to the bottom-right corner 
        that minimizes the sum of all numbers along its path. 

        Args:
        - grid (List[List[int]]): a 2D list of integers representing the grid

        Returns:
        - int: the minimum sum of all numbers along the optimal path from the top-left corner to the bottom-right corner
        """
        min_paths = [[0 for j in range(0, len(grid[0]))] for i in range(0, len(grid))]

        min_paths[0][0] = grid[0][0]
        for j in range(1, len(grid[0])):
            min_paths[0][j] = min_paths[0][j - 1] + grid[0][j]

        for i in range(1, len(grid)):
            min_paths[i][0] = min_paths[i - 1][0] + grid[i][0]
            
        
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                min_paths[i][j] = min(min_paths[i][j - 1], min_paths[i - 1][j]) + grid[i][j]
        
                
        return min_paths[len(grid) - 1][len(grid[0]) - 1]


## 64. Minimum Path Sum
