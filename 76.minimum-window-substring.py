#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
from collections import Counter
# @lc code=start
class Solution:
    def minWindowBAD(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        l = 0
        dic = Counter(t)
        res = (0,len(s)+1)
        seen = Counter()
        num_seen = 0

        for r in range(len(s)):
            if r-l >= res[1]-res[0]:
                num_seen -= 1
                seen[s[l]] -= 1
                l += 1

            if s[r] in dic:
                if seen[s[r]] < dic[s[r]]:
                    seen[s[r]] += 1
                    num_seen += 1
            
            if num_seen == len(t):
                if r-l < res[1]-res[0]:
                    res = (l,r)
                num_seen -= 1
                seen[s[l]] -= 1
                l += 1
            
            while l < r+1 and s[l] not in seen:
                l += 1 


        if res[1] == len(s)+1:
            return ""
        return s[res[0]:res[1]+1]


    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        l = 0
        dic = Counter(t)
        have, need = 0, len(dic)
        freq = Counter()
        res = (0,len(s)+1)

        for r in range(len(s)):
            if s[r] in dic:
                freq[s[r]] += 1

            if s[r] in dic and freq[s[r]] == dic[s[r]]:
                have += 1

            while have == need:
                if s[l] in freq:
                    freq[s[l]] -= 1
                    if freq[s[l]] < dic[s[l]]:
                        have -= 1
                if r-l < res[1]-res[0]:
                    res = (l,r) 
                l += 1
                
        if res[1] == len(s)+1:
            return ""
        return s[res[0]:res[1]+1]

# @lc code=end

s = "ADOBECODEBANC"
# Move left pointer only when value at pointer is found
# ADOBEC
# ADOBECODEBA
# BECODEBA
# now we have a B that is untracked

# ADOBEC
# BECODE
# CODBBA
# BANC
t = "ABC"
s = "acbbaca"
t = "aba"
obj = Solution()
print(obj.minWindow(s,t))
