# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        stack = [root]

        while stack:
            node = stack.pop()
            if not node:
                continue

            answer.append(node.val)
            stack.append(node.left)
            stack.append(node.right)

        return answer[::-1]