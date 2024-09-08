#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#
from typing import List
from collections import deque
# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        stack = deque()
        seen = {}
        m,n = len(grid), len(grid[0])
        num_oranges = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                val = grid[i][j]
                if val != 0:
                    num_oranges += 1
                if val == 2:
                    stack.append((i,j))
                    seen[(i,j)] = 0
                
        while stack:
            cur = stack.popleft()

            if cur[0] > 0:
                ind = (cur[0]-1, cur[1])
                val = grid[ind[0]][ind[1]]
                orange = (val == 1 or val == 2)
                if orange and (ind not in seen or seen[ind] > seen[cur]+1):
                    stack.append(ind)
                    seen[ind] = seen[cur]+1

            if cur[1] > 0:
                ind = (cur[0], cur[1]-1)
                val = grid[ind[0]][ind[1]]
                orange = (val == 1 or val == 2)
                if orange and (ind not in seen or seen[ind] > seen[cur]+1):
                    stack.append(ind)
                    seen[ind] = seen[cur]+1

            if cur[0] < m-1:
                ind = (cur[0]+1, cur[1])
                val = grid[ind[0]][ind[1]]
                orange = (val == 1 or val == 2)
                if orange and (ind not in seen or seen[ind] > seen[cur]+1):
                    stack.append(ind)
                    seen[ind] = seen[cur]+1

            if cur[1] < n-1:
                ind = (cur[0], cur[1]+1)
                val = grid[ind[0]][ind[1]]
                orange = (val == 1 or val == 2)
                if orange and (ind not in seen or seen[ind] > seen[cur]+1):
                    stack.append(ind)
                    seen[ind] = seen[cur]+1

        if len(seen) != num_oranges:
            return -1
        
        if len(seen) == 0:
            return 0
        
        res = float('-inf')
        for key,value in seen.items():
            if res < value:
                res = value
        
        return res

# @lc code=end

arr = [[2,1,1],[1,1,0],[0,1,1]]
obj = Solution()
obj.orangesRotting(arr)