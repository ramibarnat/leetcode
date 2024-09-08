#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#
from collections import Counter
import heapq
# @lc code=start
class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        max_heap = [[-count, char] for char, count in counter.items()]
        heapq.heapify(max_heap)

        prev = None
        res = []
        # aaabb
        while prev or max_heap:
            if max_heap:
                prev = heapq.heappop(max_heap)

            if not res or res[-1] != prev[1]:
                res.append(prev[1])
            else:
                return ""





# @lc code=end

# {a:4, b:2, c:2}
# 