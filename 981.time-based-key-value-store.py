#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#
from collections import defaultdict
# @lc code=start
class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        l,r = 0,len(self.dic[key])-1
        values = self.dic[key] # Using this increases efficiency by a lot
        res = ""

        while r >= l:
            # mid = (r+l)//2

            # This divides by 2 and rounds down by shifting bits over by one
            # Moving bits over by 1 will basically eliminate a power of 2
            # Ex: 111101 = 61
            #     011110 = 30
            #     001111 = 15
            #     000111 = 7
    
            mid = (l+r) >> 1 
            if timestamp == values[mid][0]:
                return values[mid][1]
            elif timestamp > values[mid][0]:
                res = values[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end

