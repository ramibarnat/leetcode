#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstringFirst(self, s: str) -> int:
        dic = {}
        res = 0
        l, r = 0, 0
        while r != len(s):
            if s[r] in dic and dic[s[r]] >= l:
                l = dic[s[r]]+1
            dic[s[r]] = r
            
            if r-l+1 > res:
                res = r-l+1
            r += 1
        
        return res    
        
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        res = 0
        l = 0
        for r in range(len(s)):
            if s[r] in dic and dic[s[r]] >= l:
                l = dic[s[r]]+1
            dic[s[r]] = r
            
            if r-l+1 > res:
                res = r-l+1
            r += 1
        
        return res  
                

# @lc code=end

obj = Solution()
s = "abba"

print(obj.lengthOfLongestSubstring(s))