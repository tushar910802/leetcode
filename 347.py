class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        m = [0] * (len(nums) + 1)
        cnt = collections.Counter(nums)
        for i in range(len(m)):
            m[i] = []

        for v in cnt:
            m[cnt[v]].append(v)
        res = []
        for l in (m[::-1]):
            res += l
            if len(res) >= k: break
        return res

## 347. Top K Frequent Elements