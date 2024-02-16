class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        """
        Finds the least number of unique integers in arr after removing k elements.

        Parameters:
        - arr (List[int]): The input array.
        - k (int): The number of elements to remove.

        Returns:
        - int: The least number of unique integers.
        """
        minHeap = list(collections.Counter(arr).values())
        heapq.heapify(minHeap)

        # Greedily remove the k least frequent numbers to have the least number of unique integers.
        while k > 0:
            k -= heapq.heappop(minHeap)

        return len(minHeap) + (1 if k < 0 else 0)