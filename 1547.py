class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        """
        Finds the minimum cost of cutting a rod of length `n` into pieces at the given `cuts`.

        Args:
            n: The length of the rod.
            cuts: A list of integers that represent the positions where the rod should be cut.

        Returns:
            The minimum cost of cutting the rod.
        """
        A  = sorted([0] + cuts + [n])

        @functools.lru_cache(None)
        def dp(i, j):
            if j - i <= 1:
                return 0

            return min(A[j] - A[i] + dp(i, k) + dp(k, j) for k in range(i + 1, j))

        return dp(0, len(A) - 1)

## 1547. Minimum Cost to Cut a Stick
