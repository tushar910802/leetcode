class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums == None or len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)
        f = [0 for i in range(0,n)]
        
        f[0] = nums[0]
        f[1] = max(f[0],nums[1])
        
        for i in range(2,n):
            f[i] = max(f[i-1],f[i-2] + nums[i])
        
        return f[n-1]