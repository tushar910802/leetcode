class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        """
        Return the minimum number of bits to flip to make `c` equal to the bitwise OR of `a` and `b`.

        Parameters
        ----------
        a : int
        The first integer.
        b : int
        The second integer.
        c : int
        The target integer.

        Returns
        -------
        int
        The minimum number of bits to flip.
        """
        kMaxBit = 30
        ans = 0

        for i in range(kMaxBit):
            if (c >> i & 1) == 1:
                ans += (a >> i & 1) == 0 and (b >> i & 1) == 0
            else:  # (c >> i & 1) == 0
                ans += ((a >> i & 1) == 1) + ((b >> i & 1) == 1)

        return ans

## 1318. Minimum Flips to Make a OR b Equal to c
