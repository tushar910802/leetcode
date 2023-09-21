class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        list1 = nums1 + nums2
        
        import statistics
        return statistics.median(list1)


## 4. Median of Two Sorted Arrays
