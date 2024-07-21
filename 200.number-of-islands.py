#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
from typing import List
# @lc code=start
class Solution:
    def numIslandsFirst(self, grid: List[List[str]]) -> int:
        seen = set()
        stack = []
        count = 0
        m,n = len(grid[0]),len(grid)

        for i in range(n):
            for j in range(m):
                if (i,j) not in seen and grid[i][j] == "1":
                    stack.append((i,j))
                    seen.add((i,j))
                    count += 1

                while stack:
                    x,y = stack.pop()
                    if x-1 >= 0 and grid[x-1][y] == "1" and (x-1,y) not in seen:
                        seen.add((x-1,y))
                        stack.append((x-1,y))
                    if x+1 < n and grid[x+1][y] == "1" and (x+1,y) not in seen:
                        seen.add((x+1,y))
                        stack.append((x+1,y))
                    if y-1 >= 0 and grid[x][y-1] == "1" and (x,y-1) not in seen:
                        seen.add((x,y-1))
                        stack.append((x,y-1))
                    if y+1 < m and grid[x][y+1] == "1" and (x,y+1) not in seen:
                        seen.add((x,y+1))
                        stack.append((x,y+1))

        return count

    def numIslands(self, grid: List[List[str]]) -> int:
        stack = []
        count = 0
        m,n = len(grid[0]),len(grid)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    stack.append((i,j))
                    grid[i][j] = 0
                    count += 1

                while stack:
                    x,y = stack.pop()
                    if x-1 >= 0 and grid[x-1][y] == "1":
                        grid[x-1][y] = 0
                        stack.append((x-1,y))
                    if x+1 < n and grid[x+1][y] == "1":
                        grid[x+1][y] = 0
                        stack.append((x+1,y))
                    if y-1 >= 0 and grid[x][y-1] == "1":
                        grid[x][y-1] = 0
                        stack.append((x,y-1))
                    if y+1 < m and grid[x][y+1] == "1":
                        grid[x][y+1] = 0
                        stack.append((x,y+1))

        return count
                    
                    
# @lc code=end

arr = [["1","1","1","1","0"],
       ["1","1","0","1","0"],
       ["1","1","0","0","0"],
       ["0","0","0","0","0"]]

obj = Solution()
print(obj.numIslands(arr))