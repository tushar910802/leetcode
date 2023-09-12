class Solution:
    def minDeletions(self, s: str) -> int:
        """
        Return the minimum number of characters to delete from `s` to make the frequencies of all characters unique.

        A string `s` is called good if there are no two different characters in `s` that have the same frequency.

        Parameters
        ----------
        s : str
            The string to delete characters from.

        Returns
        -------
        int
            The minimum number of characters to delete.
        """
        ans = 0
        count = collections.Counter(s)
        usedFreq = set()

        for freq in count.values():
            while freq > 0 and freq in usedFreq:
                freq -= 1  # Delete ('a' + i).
                ans += 1
            usedFreq.add(freq)

        return ans

## 1647. Minimum Deletions to Make Character Frequencies Unique
