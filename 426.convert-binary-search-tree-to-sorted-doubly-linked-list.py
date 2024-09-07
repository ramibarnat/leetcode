#
# @lc app=leetcode id=426 lang=python3
#
# [426] Convert Binary Search Tree to Sorted Doubly Linked List
#

# @lc code=start

# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        prev = None
        head = None

        def dfs(root):
            nonlocal prev,head
            if not root:
                return
            
            dfs(root.left)
            if prev:
                root.left = prev
                prev.right = root
            else:
                head = root
            prev = root
            dfs(root.right)

        dfs(root)
        prev.right = head
        head.left = prev
        return head

# @lc code=end

root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)
obj = Solution()
obj.treeToDoublyList(root)
