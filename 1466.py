import collections

class Solution:
	def minReorder(self, n: int, connections: List[List[int]]) -> int:
	    """
	    Given a number n and a list of connections between nodes,
	    this function returns the minimum number of edges that need to be reversed
	    in order to create a directed graph such that all nodes are reachable from node 0.

	    Args:
	    - n: An integer representing the number of nodes.
	    - connections: A list of list of two integers, where each list represents a connection
	      between two nodes. The connections are undirected.

	    Returns:
	    - An integer representing the minimum number of edges that need to be reversed
	      in order to create a directed graph such that all nodes are reachable from node 0.
	    """
	    lookup, graph = set(), collections.defaultdict(list)
	    for u, v in connections:
	        lookup.add(u*n+v)
	        graph[v].append(u)
	        graph[u].append(v) 
	    result = 0
	    stk = [(-1, 0)]
	    while stk:
	        parent, u = stk.pop()
	        result += (parent*n+u in lookup)
	        for v in reversed(graph[u]):
	            if v == parent:
	                continue
	            stk.append((u, v))
	    return result

## 1466. Reorder Routes to Make All Paths Lead to the City Zero