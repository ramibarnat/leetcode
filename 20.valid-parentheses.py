#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == ")" and (not stack or stack.pop() != "("):
                return False
            elif c == "]" and (not stack or stack.pop() != "["):
                return False
            elif c == "}" and (not stack or stack.pop() != "{"):
                return False
            elif c in "([{":
                stack.append(c)
        
        return not stack

# @lc code=end

s = "]"
obj = Solution()
print(obj.isValid(s))
