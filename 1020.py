class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(x, y):
            if x < 0 or x == rows or y < 0 or y == cols:
                return False, 0
            if grid[x][y] == 0:
                return True, 0
                
            grid[x][y] = 0

            l, ln = dfs(x-1, y)
            r, rn = dfs(x+1, y)
            u, un = dfs(x, y-1)
            d, dn = dfs(x, y+1)
            if l and r and u and d:
                return True, 1+ln+rn+un+dn
            else:
                return False, 0 

        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0: continue 
                valid, num = dfs(i, j)
                if valid:
                    res += num
        return res

## 1020. Number of Enclaves
        