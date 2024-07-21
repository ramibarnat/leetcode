#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
from typing import List
# @lc code=start
class Solution:
    def generateParenthesisFirst(self, n: int) -> List[str]:
        res = []
        def genParenthesis(cur, open_count, closed_count):
            if open_count == closed_count == n:
                res.append("".join(cur))
            elif open_count == n:
                cur.append(')')
                genParenthesis(cur,open_count,closed_count+1)
            elif open_count == closed_count:
                cur.append('(')
                genParenthesis(cur,open_count+1,closed_count)
            else:
                cur_copy = cur[:]
                cur_copy.append(')')
                cur.append('(')
                genParenthesis(cur,open_count+1,closed_count)
                genParenthesis(cur_copy,open_count,closed_count+1)
        
        cur = ['(']
        genParenthesis(cur,1,0)

        return res

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []

        def backtrack(open_count, closed_count):
            if open_count == closed_count == n:
                res.append("".join(cur))

            if open_count < n:
                cur.append('(')
                backtrack(open_count+1,closed_count)
                cur.pop()
            if open_count > closed_count:
                cur.append(')')
                backtrack(open_count,closed_count+1)
                cur.pop()
        
        backtrack(0,0)
        return res
# @lc code=end

obj = Solution()
print(obj.generateParenthesis(3))
