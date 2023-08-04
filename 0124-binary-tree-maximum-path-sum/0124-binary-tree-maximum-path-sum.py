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
            
            left = recursion(node.left, result) if node.left else 0
            right = recursion(node.right, result) if node.right else 0
            
            
            result[0] = max(result[0], max(left, 0) + max(right, 0) + node.val)
            
            return max(max(left, right) + node.val, node.val)
        
        
        value = recursion(root, result)
        
        return max(value, result[0])