class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        """
        Finds the minimum time needed to finish all courses, given a list of course prerequisites and the time required to complete each course.

        Args:
            n: The number of courses.
            relations: A list of course prerequisites, where each prerequisite is a list of two integers [a, b], where course a must be completed before course b.
            time: A list of integers, where time[i] is the time required to complete course i.

        Returns:
            The minimum time needed to finish all courses.
        """
        # Build a graph of the courses, where each node represents a course and each edge represents a prerequisite.

        graph = [[] for _ in range(n)]
        inDegree = [0] * n
        # Initialize the distance array, which will store the minimum time needed to finish each course.

        dist = time.copy()

        # Build graph.
        for a, b in relations:
            u = a - 1
            v = b - 1
            graph[u].append(v)
            inDegree[v] += 1

        # Topology
        q = collections.deque([i for i, d in enumerate(inDegree) if d == 0])

        while q:
            u = q.popleft()
            for v in graph[u]:
                dist[v] = max(dist[v], dist[u] + time[v])
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    q.append(v)

        return max(dist)

## 2050. Parallel Courses III