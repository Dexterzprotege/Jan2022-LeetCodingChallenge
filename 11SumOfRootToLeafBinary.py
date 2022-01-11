# Question: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

# Solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def preOrder(root, val = 0):
            if not root:
                return 0
            val = val*2 + root.val
            if root.left == None and root.right == None:
                return val
            return preOrder(root.left, val) + preOrder(root.right, val)
        return preOrder(root, 0)

# Verdict:
# Runtime: 60 ms, faster than 15.86% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.
# Memory Usage: 14.3 MB, less than 96.20% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.
