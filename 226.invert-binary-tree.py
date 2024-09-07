#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        head = root
        def dfs(root):
            if not root:
                return
            
            root.left, root.right = root.right, root.left
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return head

# @lc code=end

