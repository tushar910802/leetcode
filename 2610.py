class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        """
        Reconstructs a matrix based on the occurrences of numbers in the given list.

        Args:
        - nums (List[int]): A list of integers.

        Returns:
        - List[List[int]]: A matrix constructed based on the occurrences of numbers in the input list.

        Algorithm:
        1. Initialize an empty list 'ans' to store the matrix.
        2. Create a count list to track the occurrences of each number in 'nums'.
        3. Iterate through 'nums' and increment the count for each number.
        4. Construct 'ans' on demand while iterating through 'nums':
            - If the count of the current number exceeds the length of 'ans', append a new list to 'ans'.
            - Append the current number to the appropriate sublist in 'ans' based on its count.
        5. Return the constructed matrix 'ans'.

        Example:
        Solution().findMatrix([1, 2, 2, 3, 3, 3]) returns [[1], [2, 3], [2, 3], [3]]
        - Explanation: The input list has 1 occurrence of 1, 2 occurrences of 2, and 3 occurrences of 3.
                       The matrix is constructed with the numbers placed in sublists based on their counts.
        """
        ans = []
        count = [0] * (len(nums) + 1)

        for num in nums:
            count[num] += 1
            # Construct `ans` on demand.
            if count[num] > len(ans):
                ans.append([])
            ans[count[num] - 1].append(num)

        return ans