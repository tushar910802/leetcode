class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = -1
        if nums == None or len(nums) == 0:
            return -1
        
        min_index = self.find_min_index(nums)
        
        if nums[min_index] <= target <= nums[-1]:
            return self.binary_search(nums, target, min_index, len(nums) - 1)
        
        return self.binary_search(nums, target, 0, min_index)

        
    def find_min_index(self, nums):
        start = 0
        end = len(nums) - 1
                
        while start + 1 < end:
            mid = start + (end - start) // 2

            if nums[mid] < nums[end]:
                end = mid
            else:
                start = mid
                
        if nums[start] < nums[end]:
            return start
        
        return end
    
    def binary_search(self, nums, target, start, end):
        while start + 1 < end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid            
            elif nums[mid] < target:
                start = mid
            else:
                end = mid
                
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        
        return -1