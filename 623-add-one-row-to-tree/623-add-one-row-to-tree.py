# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        def dfs(cur, depth):
            if depth == 2:                    
                new = TreeNode(val)
                new.left = cur.left
                cur.left = new

                new = TreeNode(val)
                new.right = cur.right
                cur.right = new   
                
                return
            
            if cur.left:
                dfs(cur.left, depth-1)
            
            if cur.right:
                dfs(cur.right, depth-1)
            
        
        if depth == 1:
            new = TreeNode(val)
            new.left = root
            return new
        
        else:
            dfs(root, depth)
            return root
        
