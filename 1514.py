class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        """
        Finds the maximum probability of reaching the 'end' node from the 'start' node in a directed graph.

        Parameters:
            n (int): The total number of nodes in the graph.
            edges (List[List[int]]): A list of edges in the graph represented as pairs of nodes.
            succProb (List[float]): A list of probabilities corresponding to the success of traversing each edge.
            start (int): The starting node in the graph.
            end (int): The target node to reach in the graph.

        Returns:
            float: The maximum probability of reaching the 'end' node from the 'start' node. Returns 0 if it is not possible to reach the 'end' node.

        """
        maps = defaultdict(list)
        for i in range(len(edges)):
            maps[edges[i][0]].append((edges[i][1], succProb[i]))
            maps[edges[i][1]].append((edges[i][0], succProb[i]))
        q = [(-1, start)]
        dist = defaultdict(float)
        dist[start] = -1
        while q:
            curdist, cur = heapq.heappop(q)
            if cur == end:
                return -curdist
            for node, prob in maps[cur]:
                tmp = curdist * prob
                if tmp < dist[node]:
                    dist[node] = tmp
                    heapq.heappush(q, (tmp, node))
        return 0