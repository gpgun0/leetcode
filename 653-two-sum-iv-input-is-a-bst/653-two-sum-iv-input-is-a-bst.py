# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

      def dfs(node, Set):

        if not node:
          return False
        
        if not k-node.val in Set:
          Set.add(node.val)

        elif k-node.val in Set:
          return True

        return dfs(node.left, Set) or dfs(node.right, Set)

      return dfs(root, set([]))