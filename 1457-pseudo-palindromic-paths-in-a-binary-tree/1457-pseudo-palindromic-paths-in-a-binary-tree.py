# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def dfs(root, arr):
            l = arr.copy()
            cnt = 0
            l[root.val] += 1
            if not root.left and not root.right:
                limit = 0
                
                if sum(map(lambda x: x%2, l)) > 1:
                    return 0
                # for idx in l:
                #     if idx%2 == 1:
                #         limit += 1
                #     if limit > 1:
                #         return 0
                return 1
            
            if root.left:
                cnt += dfs(root.left, l)
                
            if root.right:
                cnt += dfs(root.right, l)
            
            return cnt
        
        answer = dfs(root, [0]*10)
        
        return answer