#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vals = set(nums)
        biggest = 0
        for val in vals:
            if val - 1 not in vals:
                count = 1
                while val + count in vals:
                    count += 1
                biggest = max(biggest, count)
        return biggest
# @lc code=end

