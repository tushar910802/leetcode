class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(v, c):
            color[v] = c
            for node in graph[v]:
                if color[node] == c:
                    return False
                if color[node] == 0 and not dfs(node, -c):
                    return False
            return True
        
        l = len(graph)
        color = [0] * l
        for i in range(l):
            if color[i] == 0:
                if not dfs(i, 1):
                    return False
        return True

## 785. Is Graph Bipartite?