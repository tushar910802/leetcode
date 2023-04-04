class Solution:
    def partitionString(self, s: str) -> int:
        """
        Returns the minimum number of substrings of the given string `s` that can be formed such that each character in a substring appears only in that substring.

        Args:
            s (str): The input string to partition.

        Returns:
            int: The minimum number of substrings of the given string `s` that can be formed such that each character in a substring appears only in that substring.
        """
        ans = 1
        usedMask = 0

        for c in s:
            i = ord(c) - ord('a')
            if usedMask >> i & 1:
                usedMask = 1 << i
                ans += 1
            else:
                usedMask |= 1 << i

        return ans

## 2405. Optimal Partition of String