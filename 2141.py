import heapq

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        """
        Maximize the running time of n computers using the given batteries.

        Args:
            n: The number of computers.
            batteries: A list of battery durations.

        Returns:
            The maximum running time of the n computers.
        """
        total = sum(batteries)
        for i in range(len(batteries)):
            batteries[i] = -batteries[i]  # max_heap
        heapq.heapify(batteries)
        while -batteries[0] > total//n:
            n -= 1
            total -= -heapq.heappop(batteries)
        return total//n

## 2141. Maximum Running Time of N Computers
