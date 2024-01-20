class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
        Calculates the sum of the minimum elements of all subarrays of the given array.

        Parameters:
        - arr (List[int]): The input array.

        Returns:
        - int: The sum of the minimum elements of all subarrays.

        Example:
        sumSubarrayMins([3, 1, 2, 4]) should return 17, as the subarrays and their
        minimum elements are [3], [1], [2], [4], [3, 1], [1, 2], [2, 4], [3, 1, 2],
        [1, 2, 4], and [3, 1, 2, 4].

        Note:
        - The function uses two arrays, prevMin and nextMin, to store the indices of
          the previous and next minimum elements for each element in the array.
        - It employs a stack to efficiently find these indices.
        - The final result is obtained by calculating the sum based on the minimum
          elements and their positions in the array.

        Complexity:
        - Time: O(N), where N is the length of the input array.
        - Space: O(N), as the function uses two arrays of size N for storage.
        """
        kMod = 1_000_000_007
        n = len(arr)
        ans = 0
        # prevMin[i] := index k s.t. arr[k] is the previous minimum in arr[:i]
        prevMin = [-1] * n
        # nextMin[i] := index k s.t. arr[k] is the next minimum in arr[i + 1:]
        nextMin = [n] * n
        stack = []

        for i, a in enumerate(arr):
            while stack and arr[stack[-1]] > a:
                index = stack.pop()
                nextMin[index] = i
            if stack:
                prevMin[i] = stack[-1]
            stack.append(i)

        for i, a in enumerate(arr):
            ans += a * (i - prevMin[i]) * (nextMin[i] - i)
            ans %= kMod

        return ans