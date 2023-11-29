class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Calculates the Hamming weight of a given integer.

        The Hamming weight is the number of '1' bits in the binary representation
        of the given integer.

        Parameters:
        - n (int): The input integer for which the Hamming weight is to be calculated.

        Returns:
        - int: The Hamming weight, i.e., the number of '1' bits in the binary representation
        of the input integer 'n'.

        Example:
        >>> hammingWeight(11)
        3
        # Explanation: The binary representation of 11 is '1011', which has 3 '1' bits.

        >>> hammingWeight(128)
        1
        # Explanation: The binary representation of 128 is '10000000', which has 1 '1' bit.
        """
        count = 0
        
        mask = 1
        for _ in range(32):
            if n & mask != 0:
                count += 1
            mask = mask << 1
            
        return count