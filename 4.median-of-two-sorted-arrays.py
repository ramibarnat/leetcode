#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
from typing import List
# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            smaller = nums1
            bigger = nums2
        else:
            smaller = nums2
            bigger = nums1

        half = (len(bigger)+len(smaller)-1) >> 1
        l,r = 0,len(smaller)-1
        while True:
            mid_s = (l+r) >> 1
            mid_b = half-mid_s-1
            if mid_s >= 0 and mid_b != len(bigger)-1 and smaller[mid_s] > bigger[mid_b+1]:
                r = mid_s - 1
            elif mid_b >= 0 and mid_s != len(smaller)-1 and bigger[mid_b] > smaller[mid_s+1]:
                r += mid_s
            else:
                if mid_s < 0: 
                    if (len(bigger)+len(smaller)%2==0):
                        return bigger[-1]
                    return (bigger[-1]+smaller[0])/2
                if mid_b < 0: 
                    if (len(bigger)+len(smaller)%2==0):
                        return smaller[-1]
                    return (smaller[-1]+bigger[0])/2
                left_max = max(bigger[mid_b],smaller[mid_s])
                if (len(bigger)+len(smaller)) % 2 == 0:
                    x = float('inf') if mid_b == len(bigger)-1 else bigger[mid_b+1]
                    y = float('inf') if mid_s == len(smaller)-1 else smaller[mid_s+1]
                    right_min = min(x,y)
                    return (right_min+left_max) / 2
                return left_max

                

# @lc code=end

a=[1,2]
b=[3,4]
obj = Solution()
print(obj.findMedianSortedArrays(a,b))