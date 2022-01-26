# Question: https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

# ----------------------------------------------------------------------------------------------------------------- #

# Solution 2: One pass, two stacks
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        stack1, stack2, result = [], [], []
        tree1, tree2 = root1, root2        
        while tree1 or tree2 or stack1 or stack2:
            while tree1:
                stack1.append(tree1)
                tree1 = tree1.left
            while tree2:
                stack2.append(tree2)
                tree2 = tree2.left
            if not stack2 or (stack1 and stack1[-1].val <= stack2[-1].val):
                tree1 = stack1.pop()
                result.append(tree1.val)
                tree1 = tree1.right
            else:
                tree2 = stack2.pop()
                result.append(tree2.val)
                tree2 = tree2.right
        return result

# Verdict:
# Runtime: 528 ms, faster than 33.89% of Python3 online submissions for All Elements in Two Binary Search Trees.
# Memory Usage: 18 MB, less than 89.21% of Python3 online submissions for All Elements in Two Binary Search Trees.

# ----------------------------------------------------------------------------------------------------------------- #

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

# ----------------------------------------------------------------------------------------------------------------- #
