class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        """
            Args:
        - colors (str): A string representing the color of each node in the graph. The string consists
                        of lowercase English letters.
        - edges (List[List[int]]): A list of edges in the graph. Each edge is represented by a list 
                                of two integers, the source node and the target node.

        Returns:
        - int: The largest path value of the given graph, if there exists a path that traverses all 
            nodes exactly once. Otherwise, returns -1.

        The function first builds a graph from the given edges and color information, and then performs
        a topological sort to traverse the graph. At each node visited during the traversal, the function
        updates a count array that keeps track of the number of occurrences of each color along the path
        to that node. The function returns the maximum value in this count array.
        """
        n = len(colors)
        colorCount = [[0] * 26 for _ in range(n)]  
        maxColorNum = 0
        colorbase = ord('a')
        
        for e in edges:
            g[e[0]].append(e[1])
        
        visted = [False] * n

        def dfs(i, pathNodes: set):
            nonlocal maxColorNum
            visted[i] = True
            pathNodes.add(i)
            for nexti in g[i]:
                if nexti in pathNodes:  
                    maxColorNum = -1
                    return
                if not visted[nexti]:
                    dfs(nexti, pathNodes)
                    if maxColorNum < 0:  
                        return
                for j in range(26):  
                    colorCount[i][j] = max(colorCount[i][j], colorCount[nexti][j])
            color = ord(colors[i]) - colorbase
            colorCount[i][color] += 1  
            maxColorNum = max(maxColorNum, colorCount[i][color])
            pathNodes.remove(i)

        for i in range(n):
            if not visted[i]:
                dfs(i, set())
            if maxColorNum < 0:
                break
        return maxColorNum