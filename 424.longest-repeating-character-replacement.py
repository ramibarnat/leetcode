#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#
from collections import defaultdict

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # dic = {A: 3, B: 1}
        # as soon as more than one other letter is seen, we
        # have to stop since k = 1 so we can only swap one letter

        # s = "AABABBA", k = 1
        # l = 0, r = 0
        # s[r] = A, most = (A,1), res = 1
        # l = 0, r = 1
        # a = 1
        # if we find a letter that is not our most, we need
        # to subtract from our k value

        dic = defaultdict(int)
        l = 0
        res = 0
        most = s[0]
        # count = k
        # AABABBA, k = 1
        # A|ABAB|BA
        # 
        for r in range(len(s)):
            dic[s[r]] += 1
            if s[r] != most:
                if dic[s[r]] > dic[most]:
                    most = s[r]
                elif (r-l+1)-dic[most] > k:
                    while (r-l+1)-dic[most] > k:
                        dic[s[l]] -= 1

                        if s[l] == most:
                            for key, val in dic.items():
                                if val > dic[s[l]]:
                                    most = key
                                    break
                        l += 1
                    
            if r-l+1 > res:
                res = r-l+1
                    
        return res

# @lc code=end

s = "AABABBA"
k = 1
obj = Solution()
print(obj.characterReplacement(s,k))