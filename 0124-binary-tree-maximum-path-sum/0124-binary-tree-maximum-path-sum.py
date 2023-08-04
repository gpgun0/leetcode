# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = [-1000]
        
        def recursion(node, result):
            
            left = max(recursion(node.left, result), 0) if node.left else 0
            right = max(recursion(node.right, result), 0) if node.right else 0
            
            result[0] = max(result[0], left + right + node.val)
            
            return max(left, right) + node.val
        
        value = recursion(root, result)
        
        return max(value, result[0])