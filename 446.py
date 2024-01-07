class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
        Counts the number of arithmetic slices in the given list of integers.

        Args:
        - nums (List[int]): A list of integers.

        Returns:
        - int: The count of arithmetic slices in the input list.

        Algorithm:
        1. Initialize a list of dictionaries 'arithmetic_count' to store the count of arithmetic sequences ending at each index with a specific difference.
        2. Initialize the 'total_count' variable to 0, which will accumulate the total count of arithmetic sequences.
        3. Iterate over each pair (i, x) in 'nums', where 'i' is the index and 'x' is the number.
        4. For each pair, iterate over all the numbers before the current number.
        5. Calculate the difference ('difference') between the current and previous numbers.
        6. Add the count of arithmetic sequences ending at index 'j' with the same difference to the 'total_count'.
        7. Increment the count of arithmetic sequences ending at index 'i' with the same difference.
           This count will be one more than the count at index 'j' since 'i' extends the sequence from 'j' by one more element.
        8. Return the 'total_count', which represents the total count of arithmetic sequences found in 'nums'.

        Example:
        Solution().numberOfArithmeticSlices([1, 2, 3, 4]) returns 3
        - Explanation: There are three arithmetic slices: [1, 2, 3], [2, 3, 4], and [1, 2, 3, 4].
        """
        arithmetic_count = [defaultdict(int) for _ in nums]
      
        # Initialize the answer to 0
        total_count = 0
      
        # Iterate over each pair (i, x) where `i` is the index and `x` is the number
        for i, current_num in enumerate(nums):
            # Iterate over all the numbers before the current number
            for j, prev_num in enumerate(nums[:i]):
                # Calculate the difference between the current and previous number
                difference = current_num - prev_num
              
                # Add the count of arithmetic sequences ending at index `j` with the same difference to the answer
                total_count += arithmetic_count[j][difference]
              
                # Add or increment the count of arithmetic sequences ending at index `i` with the same difference
                # It will be 1 more than the count at index `j` since `i` extends the sequence from `j` by one more element
                arithmetic_count[i][difference] += arithmetic_count[j][difference] + 1

        # Return the total count of all arithmetic sequences found in `nums`
        return total_count
