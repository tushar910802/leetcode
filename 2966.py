class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        """
        Divides the given sorted array into triplets where the difference between
        consecutive elements is at most k.

        Parameters:
        - nums (List[int]): A sorted list of integers.
        - k (int): The maximum allowed difference between consecutive elements in a triplet.

        Returns:
        - List[List[int]]: A list of triplets satisfying the given condition.

        Example:
        divideArray([1, 2, 3, 5, 8, 9, 10], 2) should return [[1, 2, 3], [5, 8, 9]],
        as these are the triplets with differences at most 2.

        Note:
        - The function first sorts the input array.
        - It then iterates through the sorted array, creating triplets where the
          difference between consecutive elements is at most k.
        - The result is a list of triplets satisfying the given condition.

        Complexity:
        - Time: O(N log N), where N is the length of the input array due to sorting.
        - Space: O(1), as the function only uses constant space for variables.
        """
        ans = []

        nums.sort()

        for i in range(2, len(nums), 3):
            if nums[i] - nums[i - 2] > k:
                return []
            ans.append([nums[i - 2], nums[i - 1], nums[i]])

        return ans