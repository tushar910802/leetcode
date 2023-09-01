class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        Count the number of 1's in the binary representation of a number.

        Parameters
        ----------
        n : int
            The number to count the 1's in.

        Returns
        -------
        List[int]
            A list of the number of 1's in the binary representation of each number from 0 to n.
        """
        # Let f(i) := i's # Of 1's in bitmask
        # f(i) = f(i / 2) + i % 2
        ans = [0] * (n + 1)

        for i in range(1, n + 1):
            ans[i] = ans[i // 2] + (i & 1)

        return ans
        
## 338. Counting Bits