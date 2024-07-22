#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
import time
import os
from typing import List
# @lc code=start
class Solution:
    # def numIslandsFirst(self, grid: List[List[str]]) -> int:
    #     seen = set()
    #     stack = []
    #     count = 0
    #     m,n = len(grid[0]),len(grid)

    #     for i in range(n):
    #         for j in range(m):
    #             if (i,j) not in seen and grid[i][j] == "1":
    #                 stack.append((i,j))
    #                 seen.add((i,j))
    #                 count += 1

    #             while stack:
    #                 x,y = stack.pop()
    #                 if x-1 >= 0 and grid[x-1][y] == "1" and (x-1,y) not in seen:
    #                     seen.add((x-1,y))
    #                     stack.append((x-1,y))
    #                 if x+1 < n and grid[x+1][y] == "1" and (x+1,y) not in seen:
    #                     seen.add((x+1,y))
    #                     stack.append((x+1,y))
    #                 if y-1 >= 0 and grid[x][y-1] == "1" and (x,y-1) not in seen:
    #                     seen.add((x,y-1))
    #                     stack.append((x,y-1))
    #                 if y+1 < m and grid[x][y+1] == "1" and (x,y+1) not in seen:
    #                     seen.add((x,y+1))
    #                     stack.append((x,y+1))

    #     return count

    def printArrOld(self, grid: List[List[str]], spot, count) -> None:
        time.sleep(0.5)
        os.system('cls')
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) == spot:
                    print('|'+grid[i][j]+'|', end="")
                elif (i,j+1) == spot:
                    if j == 0:
                        print(" " + grid[i][j], end="")
                    else: 
                        print(grid[i][j], end="")
                elif j == 0 and (i,j) != spot:
                    print(" " + grid[i][j], end=" ")
                else:
                    print(grid[i][j], end=" ")

                if i == 0 and j == len(grid[0])-1:
                    print(f"     Num of Islands: {count}", end="")
            print()

        print()

    def printArr(self, grid: List[List[str]], spot, count) -> None:
        time.sleep(0.5)
        os.system('cls')
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) == spot:
                    if grid[i][j] == '1':
                        print("\033[92m1\033[0m", end=" ")
                    else:
                        print("\033[91m0\033[0m", end=" ")
                else:
                    print(grid[i][j],end=" ")
                
                if i == 0 and j == len(grid[0])-1:
                    print(f"     Num of Islands: {count}", end="")
            print()


    def numIslands(self, grid: List[List[str]]) -> int:
        stack = []
        count = 0
        m,n = len(grid[0]),len(grid)

        for i in range(n):
            for j in range(m):
                self.printArr(grid,(i,j),count)

                if grid[i][j] == "1":
                    count += 1
                    stack.append((i,j))
                    grid[i][j] = '0'
                    self.printArr(grid,(i,j),count)

                while stack:
                    x,y = stack.pop()
                    if x-1 >= 0 and grid[x-1][y] == "1":
                        self.printArr(grid,(x-1,y),count)
                        grid[x-1][y] = '0'
                        self.printArr(grid,(x-1,y),count)
                        stack.append((x-1,y))
                    if x+1 < n and grid[x+1][y] == "1":
                        self.printArr(grid,(x+1,y),count)
                        grid[x+1][y] = '0'
                        self.printArr(grid,(x+1,y),count)
                        stack.append((x+1,y))
                    if y-1 >= 0 and grid[x][y-1] == "1":
                        self.printArr(grid,(x,y-1),count)
                        grid[x][y-1] = '0'
                        self.printArr(grid,(x,y-1),count)
                        stack.append((x,y-1))
                    if y+1 < m and grid[x][y+1] == "1":
                        self.printArr(grid,(x,y+1),count)
                        grid[x][y+1] = '0'
                        self.printArr(grid,(x,y+1),count)
                        stack.append((x,y+1))


        return count
                    
                    
# @lc code=end

arr = [["1","1","1","1","0","1","1","0","0"],
       ["1","1","0","1","0","1","0","0","1"],
       ["1","1","0","0","0","0","1","0","1"],
       ["0","0","0","1","1","0","1","1","1"]]

obj = Solution()
print(obj.numIslands(arr))