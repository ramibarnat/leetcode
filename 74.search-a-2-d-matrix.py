#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
from typing import List
# @lc code=start
class Solution:
    def searchMatrixWRONG(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix[0])
        n = len(matrix)
        l = (0,0)
        r = (n-1,m-1)
        
        # This is NOT log(m) + log(n), this is log(m*n) which is worse
        while (r[1] >= l[1] and r[0] == l[0]) or r[0] > l[0]:
            mid = ((r[0]*m + r[1]) + (l[0]*m + l[1])) // 2
            mid_ind = (mid // m, mid % m)
            if matrix[mid_ind[0]][mid_ind[1]] == target:
                return True
            elif matrix[mid_ind[0]][mid_ind[1]] < target:
                mid += 1
                l = (mid // m, mid % m)
            else:
                mid -= 1
                r = (mid // m, mid % m)
        
        return False
            
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix[0])
        n = len(matrix)
        top = n - 1
        bot = 0

        while top >= bot:
            mid = (top+bot)//2
            if matrix[mid][0] > target:
                top = mid - 1
            elif matrix[mid][m-1] < target:
                bot = mid + 1
            else:
                l,r = 0, m-1
                while r >= l:
                    cur = (r+l)//2
                    if matrix[mid][cur] == target:
                        return True
                    if matrix[mid][cur] > target:
                        r = cur - 1
                    else:
                        l = cur + 1
                return False
            

# @lc code=end

mat = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
mat = [[1]]
target = 1
obj = Solution()
print(obj.searchMatrix(mat, target))
