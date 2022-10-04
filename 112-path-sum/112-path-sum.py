# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        answer = [False]
        def dfs(node, path):
            path = path.copy()
            
            if not node:
                return
            
            path.append(node.val)
            
            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)
                
            if not node.left and not node.right:
                if sum(path) == targetSum:
                    answer[0] = True
                
        dfs(root, [])
        return answer[0]