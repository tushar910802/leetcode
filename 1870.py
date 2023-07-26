class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        """
        This function takes a list of distances and a time limit, and returns the minimum speed needed to reach the destination within the time limit.

        Args:
            dist: A list of distances.
            hour: The time limit in hours.

        Returns:
            The minimum speed needed to reach the destination within the time limit.

        Example:
            >>> minSpeedOnTime([10, 20, 30], 1)
            20
        """
        ans = -1
        l = 1
        r = int(1e7)

        def time(speed: int) -> float:
            summ = 0
            for i in range(len(dist) - 1):
                summ += math.ceil(dist[i] / speed)
            return summ + dist[-1] / speed

        while l <= r:
            m = (l + r) // 2
            if time(m) > hour:
                l = m + 1
            else:
                ans = m
                r = m - 1

        return ans

## 1870. Minimum Speed to Arrive on Time
