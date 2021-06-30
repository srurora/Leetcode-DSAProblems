# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        if not root.right: return self.maxDepth(root.left)+1
        if not root.left: return self.maxDepth(root.right)+1
        return max(self.maxDepth(root.right),self.maxDepth(root.left))+1