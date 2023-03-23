class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        """
        Given n nodes labeled from 0 to n-1 and a list of undirected connections,
        this function returns the minimum number of cables required to connect all the nodes.

        Args:
        - n: An integer representing the number of nodes.
        - connections: A list of list of two integers, where each list represents an undirected connection
        between two nodes.

        Returns:
        - An integer representing the minimum number of cables required to connect all the nodes.
        If it's impossible to connect all the nodes, the function returns -1.
        """
        def find(x):
            """
            This is a helper function that finds the parent node of a given node x.
            If the parent of node x is not itself, this function applies path compression
            to improve the efficiency of future find operations.

            Args:
            - x: An integer representing the node whose parent node is to be found.

            Returns:
            - An integer representing the parent node of the given node x.
            """
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        cnt = 0
        p = list(range(n))
        for a, b in connections:
            if find(a) == find(b):
                cnt += 1
            else:
                p[find(a)] = find(b)
                n -= 1
        return -1 if n - 1 > cnt else n - 1


## 1319. Number of Operations to Make Network Connected