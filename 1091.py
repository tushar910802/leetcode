class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        Finds the shortest path from the top-left corner to the bottom-right corner of a binary matrix.

        Args:
            grid: A 2D list of integers, where a 0 represents an open space and a 1 represents a wall.

        Returns:
            The length of the shortest path, or -1 if there is no path.
        """
        dirs = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
        row,col = len(grid),len(grid[0])
        if grid[0][0] or grid[-1][-1]:
            return -1
        if row == 1 and grid[0][0] == 0:
            return 1
        q = collections.deque()
        q.append((0,0))
        visited = set()
        visited.add((0,0))
        step = 1
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx< row and 0<= ny < col and grid[nx][ny] == 0 and (nx,ny) not in visited:
                        visited.add((nx,ny))
                        q.append((nx,ny))
                        if nx == row-1 and ny == col-1:
                            return step + 1
            step += 1
        return -1

## 1091. Shortest Path in Binary Matrix