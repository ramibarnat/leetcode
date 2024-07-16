#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

from collections import deque
from typing import List

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # nums = [1,3,-1,-3,5,3,6,7], k = 3
        # [|1,3,-1|,-3,5,3,6,7] arr = [3,-1] res = [3] only keep the number after if it's lower
        # [1,|3,-1,-3|,5,3,6,7] arr = [3,-1,-3] res = [3,3]
        # [1,3,|-1,-3,5|,3,6,7] arr = [5] res = [3,3,5]
        # [1,3,-1,|-3,5,3|,6,7] arr = [5,3] res = [3,3,5,5]
        # [1,3,-1,-3,|5,3,6|,7] arr = [6] res = [3,3,5,5,6]
        # [1,3,-1,-3,5,|3,6,7|] arr = [7] res = [3,3,5,5,6,7]

        arr = deque() # We could store indices instead to improve efficiency
        res = []
        
        for i in range(len(nums)):
            if arr and i >= k-1 and nums[i-k] == arr[0]:
                arr.popleft()
                
            while arr and arr[-1] < nums[i]:
                arr.pop()
            arr.append(nums[i])
            
            if i >= k-1: 
                res.append(arr[0])
        
        return res

# @lc code=end

nums = [1,3,-1,-3,5,3,6,7]
k = 3
obj = Solution()
print(obj.maxSlidingWindow(nums,k))