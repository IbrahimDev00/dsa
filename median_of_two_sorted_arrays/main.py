class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s = nums1+nums2
        s.sort()
        l = len(s)
        if l%2 == 0:
            return (s[l//2-1]+s[l//2]) / 2.0
        else:
            return (s[l//2])