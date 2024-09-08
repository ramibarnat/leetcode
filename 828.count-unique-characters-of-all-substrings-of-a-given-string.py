#
# @lc app=leetcode id=828 lang=python3
#
# [828] Count Unique Characters of All Substrings of a Given String
#
from collections import defaultdict
from collections import deque
# @lc code=start
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        prev = {}
        res = 0

        for i, char in enumerate(s):
            if char not in prev:
                prev[char] = deque()
                prev[char].append(-1)
            prev[char].appendleft(i)
        print(prev)
    
        for i, char in enumerate(s):
            previous = prev[char].pop()
            if len(prev[char]) > 1:
                next = prev[char][-2]
                print(next)
            else:
                next = len(s)
            res += (i-previous) * (next-i)
        
        return res
# @lc code=end
# 0-(-1) * 3-0 = 3
# 1-(-1) * 3-1 = 4
# 2-(-1) * 3-2 = 3

# 2-(-1) * 5-2
# 
s = "ABC" # A: 3, B: 4, C: 3
obj = Solution()
print(obj.uniqueLetterString(s))