class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        Reorganize String

        Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

        If it is not possible to rearrange the characters, return an empty string.

        Example 1:

        Input: s = "aab"
        Output: "aba"

        Example 2:

        Input: s = "aabb"
        Output: ""

        Constraints:

        1 <= s.length <= 500
        s consists of only lowercase English letters.
        """

        count = collections.Counter(s)
        if max(count.values()) > (len(s) + 1) // 2:
            return ''

        ans = []
        maxHeap = [(-freq, c) for c, freq in count.items()]
        heapq.heapify(maxHeap)
        prevFreq = 0
        prevChar = '@'

        while maxHeap:
            # Get the most freq letter.
            freq, c = heapq.heappop(maxHeap)
            ans.append(c)
            # Add the previous letter back so that any two adjacent characters are not
            # the same.
            if prevFreq < 0:
                heapq.heappush(maxHeap, (prevFreq, prevChar))
            prevFreq = freq + 1
            prevChar = c

        return ''.join(ans)


## 767. Reorganize String