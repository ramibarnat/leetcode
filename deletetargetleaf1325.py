def removeLeafNodes(root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val == target:
            return None
        root.left = removeLeafNodes(root.left, target)
        root.right = removeLeafNodes(root.right, target)
        return root

removeLeafNodes([1,3,3,3,2], 3)