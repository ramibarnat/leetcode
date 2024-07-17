#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
from typing import List
import math
# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.lstrip('-').isdigit():
                stack.append(int(token))
            else:
                val2 = stack.pop()
                val1 = stack.pop()
                if token == '+':
                    stack.append(val1+val2)
                elif token == '-':
                    stack.append(val1-val2)
                elif token == '*':
                    stack.append(val1*val2)
                elif token == '/':
                    stack.append(int(val1/val2))
        
        return stack[0]

    # This is actually slower because of the additional overhead
    # associated with the error handling as opposed to using
    # traditional logic checks

    # def evalRPN(self, tokens: List[str]) -> int:
    #     stack = []
    #     for token in tokens:
    #         try:
    #             stack.append(int(token))
    #         except ValueError:
    #             val2 = stack.pop()
    #             val1 = stack.pop()
    #             if token == '+':
    #                 stack.append(val1+val2)
    #             elif token == '-':
    #                 stack.append(val1-val2)
    #             elif token == '*':
    #                 stack.append(val1*val2)
    #             elif token == '/':
    #                 stack.append(int(val1/val2))
        
    #     return stack[0]
# @lc code=end

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
obj = Solution()
print(obj.evalRPN(tokens))