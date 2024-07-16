#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:
    # [4,3,-1,4,-2,9]
    # min_vals = [4] push(4)
    # min_vals = [4,3] push(3)
    # min_vals = [4,3,-1] push(-1)
    # min_vals = [4,3,-1] push(4) push(2) push(3) push(0) push(-1) pop()

    def __init__(self):
        self.arr = []
        self.min_vals = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if not self.min_vals or val <= self.min_vals[-1]:
            self.min_vals.append(val)

    def pop(self) -> None:
        if self.arr[-1] == self.min_vals[-1]:
            self.min_vals.pop()
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.min_vals[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

