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
            if not cur:
                return 
            copied = path.copy()
            copied.append(cur.val)
            
            if not cur.left and not cur.right:
                if sum(copied) == targetSum:
                    answer.append(copied)
                return
            
            if cur.left:
                dfs(cur.left, copied)
            if cur.right:
                dfs(cur.right, copied)

            
        dfs(root, [])
        
        return answer