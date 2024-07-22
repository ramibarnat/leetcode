#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#
from typing import List
# @lc code=start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = list(zip(position,speed))
        combined.sort(key=lambda x: -x[0])
        print(combined)
        seen = set()
        count = 0

        for i,car in enumerate(combined):
            if car not in seen:
                count += 1
            
            if i != 0 and combined[i+1][1] > car[1]:
                intersect = car[0] + car[1]*(car[0]-combined[i+1][0]) / (combined[i+1][1]-car[1])
                if intersect <= target:
                    seen.add(combined[i+1])

        return count
# @lc code=end

position = [10,8,0,5,3]
speed = [2,4,1,1,3]
target = 12

obj = Solution()
print(obj.carFleet(target,position,speed))