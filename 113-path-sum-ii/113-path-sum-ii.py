# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        answer = []
        
        def dfs(cur, path):
            copied = path.copy()
            if not cur:
                return
            
            copied.append(cur.val) 
          
            dfs(cur.left, copied)
            dfs(cur.right, copied)
            
            if not cur.left and not cur.right:
                
                if sum(copied) == targetSum:
                    answer.append(copied)
                return              
            
        dfs(root, [])
        
        return answer