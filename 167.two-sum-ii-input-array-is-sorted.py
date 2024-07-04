#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l+1,r+1]
            elif total > target:
                r -= 1
            else:
                l += 1
        
# @lc code=end

obj = Solution()
arr = [2,7,11,15]
t = 9
obj.twoSum(arr, t)