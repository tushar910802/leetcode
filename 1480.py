class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=[]
        tmp=0
        for i in nums:
            tmp+=i
            ans.append(tmp)
        return ans