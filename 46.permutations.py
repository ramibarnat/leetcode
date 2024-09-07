#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
from typing import List
# @lc code=start

#     1    2
#    /|   /|
#   2 3  1 3
#   | |  | |
#   3 2  3 1

# [1,2,3]
# 1: [2,3]
class Solution:
    # For [1,2,3]
    # Iterate through numbers in list, starting at 1,
    
    # Add 1 to current array that we're creating.
    # Backtrack now using the array [1]

    # Check if 1 is in array already, move to 2
    # Add 2 to array and then backtrack again

    # Now 3 is the only number left to add, so we backtrack
    # again and add it to the results array

    # We return to the state [1,2,3], remove 3, loop ends

    # We return to [1,2], remove 2, we are still iterating through
    # the loop so we now add 3 to the end: [1,3]

    # We Backtrack again, adding only the numbers that are not in
    # [1,3], finally backtracking all the way to the state of [1],
    # where we remove 1 and then continue in the loop to add next val: [2]
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(current):
            if len(current) == len(nums):
                res = current[:]
                result.append(res)
                return
            
            for num in nums:
                if num not in current:
                    current.append(num)

                    backtrack(current)

                    current.pop()


        backtrack([])
        return result

# @lc code=end

nums = [1,2,3]
obj = Solution()
obj.permute(nums)