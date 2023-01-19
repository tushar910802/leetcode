class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        prefix = 0
        count = [1] + [0] * (k - 1)

        for a in nums:
            prefix = (prefix + a) % k
            ans += count[prefix]
            count[prefix] += 1

        return ans