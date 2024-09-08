#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#
from typing import List
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        if len(nums) == 1 and target == nums[0]:
            return 0
        
        while l<=r:
            mid = (r+l)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid-1
            else:
                l = mid+1
        
        return -1
# @lc code=end

arr = [-1,0,3,5,9,12]
t = 2

obj = Solution()
print(obj.search(arr,t))

