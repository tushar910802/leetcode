class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        """Returns the indices of the k weakest rows in the matrix `mat`, sorted in ascending order.

        Args:
            mat: A list of lists, where each row represents a group of soldiers and each column represents the number of soldiers in a regimental unit.
            k: The number of weakest rows to return.

        Returns:
            A list of integers, representing the indices of the k weakest rows in `mat`.
        """
        candidates = []

        for i, row in enumerate(mat):
            candidates.append([sum(row), i])

        candidates.sort(key=lambda c: (c[0], c[1]))

        return [i for _, i in candidates[:k]]


## 1337. The K Weakest Rows in a Matrix