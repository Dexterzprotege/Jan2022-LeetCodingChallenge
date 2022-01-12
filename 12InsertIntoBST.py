# Question: https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Solution 2: Iterative O(N) +O(1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        curr = root
        while True:
            if val > curr.val:
                if curr.right is not None:
                    curr = curr.right
                else:
                    curr.right = TreeNode(val)
                    break
            else:
                if curr.left is not None:
                    curr = curr.left
                else:
                    curr.left = TreeNode(val)
                    break
        return root

# Verdict:
# Runtime: 198 ms, faster than 18.49% of Python3 online submissions for Insert into a Binary Search Tree.
# Memory Usage: 16.7 MB, less than 85.25% of Python3 online submissions for Insert into a Binary Search Tree.

# Solution 1: Recursive O(N) + O(H)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else: 
            root.left = self.insertIntoBST(root.left, val)
        return root

# Verdict:
# Runtime: 265 ms, faster than 5.06% of Python3 online submissions for Insert into a Binary Search Tree.
# Memory Usage: 16.7 MB, less than 59.81% of Python3 online submissions for Insert into a Binary Search Tree. 
