#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
from typing import List
# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                ind = stack.pop()
                res[ind] = i-ind

            stack.append(i)
        
        return res
         
                
# @lc code=end

temperatures = [73,74,75,71,69,72,76,73]
obj = Solution()
print(obj.dailyTemperatures(temperatures))