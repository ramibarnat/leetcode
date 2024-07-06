#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
from typing import List


class Solution:
    def maxAreaWrong(self, height: List[int]) -> int:
        end = 0
        cur_area = 0
        for i, val in enumerate(height):
            if (val - height[end]) + (i - end) >= 0:
                end = i
        for i, val in enumerate(height):
            new_area = (end-i)*min(height[end],val)
            if new_area >= cur_area:
                cur_area = new_area

        return cur_area
    
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_area = -1
        while r > l:
            if min(height[l],height[r]) * (r-l) > max_area:
                max_area = min(height[l],height[r]) * (r-l)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area



# @lc code=end

arr = [2,3,4,5,18,17,6]
# arr = [1,1]
obj = Solution()
print(obj.maxArea(arr))
# min(1, 6) = 1, 2-0 = 2, a = 2
# start = 0 end = 0, cur_area = 0-0 * 1-1 = 0
# check end first
# 
# 