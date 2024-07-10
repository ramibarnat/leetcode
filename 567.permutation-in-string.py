#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#
from collections import defaultdict
from collections import Counter
# @lc code=start
class Solution:
    def checkInclusionFirst(self, s1: str, s2: str) -> bool:
        dic = defaultdict(int)
        l = 0
        for c in s1:
            dic[c] += 1
        
        letters = defaultdict(int)
        for r in range(len(s2)):
            letters[s2[r]] += 1
            if s2[r] not in dic: 
                l = r + 1
                letters = defaultdict(int)
            else:
                while letters[s2[r]] > dic[s2[r]]:
                    letters[s2[l]] -= 1
                    l += 1
            
            if r-l+1 == len(s1):
                return True

        return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic = Counter(s1)
        l = 0
        
        letters = Counter()
        for r in range(len(s2)):
            letters[s2[r]] += 1
            if s2[r] not in dic: 
                l = r + 1
                letters = Counter()
            else:
                while letters[s2[r]] > dic[s2[r]]:
                    letters[s2[l]] -= 1
                    l += 1
            
            if r-l+1 == len(s1):
                return True

        return False

# @lc code=end

s1 = "adc"
s2 = "dcda"
obj = Solution()
print(obj.checkInclusion(s1,s2))