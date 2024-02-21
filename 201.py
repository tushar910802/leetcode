class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
        Finds the bitwise AND of all numbers in the range [left, right].

        Parameters:
        - left (int): The left bound of the range.
        - right (int): The right bound of the range.

        Returns:
        - int: The bitwise AND of all numbers in the range.
        """
        return self.rangeBitwiseAnd(left >> 1, right >> 1) << 1 if left < right else left