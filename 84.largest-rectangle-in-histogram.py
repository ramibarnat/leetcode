#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
from typing import List
from collections import Counter
# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i,height in enumerate(heights):
            last_ind = i
            while stack and stack[len(stack)-1][1] > height:
                prod = (i-stack[len(stack)-1][0])*stack[len(stack)-1][1]
                if prod > res:
                    res = prod
                
                last_ind = stack.pop()[0]
            
            stack.append((last_ind,height))

        while stack:
            last = stack.pop()
            prod = (len(heights)-last[0])*last[1]
            if prod > res:
                res = prod

        return res
# @lc code=end

heights = [2,1,5,6,2,3]
heights = [2,4]
obj = Solution()
print(obj.largestRectangleArea(heights))