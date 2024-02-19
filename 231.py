class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        Determines if a given integer is a power of two.

        Parameters:
        - n (int): The integer to check.

        Returns:
        - bool: True if n is a power of two, False otherwise.
        """
        # Handle edge cases
        if n <= 0:
            return False
        
        # Keep dividing n by 2 until it becomes 1 or not divisible by 2
        while n % 2 == 0:
            n //= 2
        
        # If n is 1, then it's a power of two, otherwise not
        return n == 1
