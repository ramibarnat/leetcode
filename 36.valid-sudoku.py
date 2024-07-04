#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # {8: {0},{0},{1}}
        # {8: [{0,1},{0,5},{1,2}]}
        # dic = defaultdict(list)
        dic = {}
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val == '.':
                    continue
                box = (i//3, j//3)
                if val in dic:
                    if i in dic[val][0] or j in dic[val][1] or box in dic[val][2]:
                        return False
                    dic[val][0].add(i)
                    dic[val][1].add(j)
                    dic[val][2].add(box)
                else:
                    dic[val] = [set([i]), set([j]), set([box])]

        return True

# arr = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

# obj = Solution()
# print(obj.isValidSudoku(arr))
# @lc code=end

