# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        answer = [False]
        l = []
        
        def dfs(node, l):
            
            if not k-node.val in l:
                l.append(node.val)
            
            elif k-node.val in l:
                answer[0] = True
            
            if node.left:
                dfs(node.left, l)
            if node.right:
                dfs(node.right, l)
        
        dfs(root, [])
        
        return answer[0]