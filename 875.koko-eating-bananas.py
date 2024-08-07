#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#
from collections import List
from math import ceil
# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans = float('inf')
        l, r = 1, max(piles)
        while r >= l:
            mid = (l+r)//2
            hrs = 0
            for pile in piles:
                hrs += ceil(pile/mid)

            if hrs > h:
                l = mid + 1
            else:
                r = mid - 1
                if mid < ans:
                    ans = mid
        
        return ans


# @lc code=end

