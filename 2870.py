class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        Calculates the minimum number of operations needed to make all elements in 'nums' equal,
        given that an operation consists of incrementing any element by 1.

        Args:
        - nums (List[int]): A list of integers.

        Returns:
        - int: The minimum number of operations needed to make all elements in 'nums' equal.
               Returns -1 if it is impossible to make all elements equal.

        Algorithm:
        1. Count the occurrences of each number in 'nums'.
        2. If any number occurs only once, it's impossible to make all elements equal, return -1.
        3. Calculate the total operations needed:
            - For each frequency, calculate the number of operations needed to make that frequency to 0 mod 3.
            - Sum up these calculated operations for all frequencies.
        4. Return the total operations calculated.

        Example:
        Solution().minOperations([1, 2, 2, 3, 4, 4, 5, 6]) returns 5
        - Explanation: The frequencies are Counter({2: 2, 4: 2, 1: 1, 3: 1, 5: 1, 6: 1}).
                       To make all elements equal, 5 operations are needed:
                       2 operations for 2s, 2 operations for 4s, and 1 operation for 1, 3, 5, and 6.
        """
        count = collections.Counter(nums)
        if 1 in count.values():
            return -1
        return sum((freq + 2) // 3 for freq in count.values())