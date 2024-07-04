#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
from collections import deque


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # race car
        # 

        left = 0
        right = len(s) - 1

        while right > left:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
            
        return True

        

# @lc code=end

