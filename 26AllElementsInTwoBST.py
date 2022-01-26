# Question: https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

# Solution 1: Brute Force:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ans = []
        def inOrder(root):
            if root is None:
                return 
            inOrder(root.left)
            ans.append(root.val)
            inOrder(root.right)
        inOrder(root1)
        inOrder(root2)
        return sorted(ans)

# Verdict:
# Runtime: 328 ms, faster than 84.57% of Python3 online submissions for All Elements in Two Binary Search Trees.
# Memory Usage: 22.7 MB, less than 21.43% of Python3 online submissions for All Elements in Two Binary Search Trees.
