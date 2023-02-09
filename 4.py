class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        list1 = nums1 + nums2
        print(list1)
        import statistics
        return statistics.median(list1)