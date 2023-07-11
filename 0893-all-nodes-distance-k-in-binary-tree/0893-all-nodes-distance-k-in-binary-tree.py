# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        def bind_node(cur, parent):
            if cur and parent:
                graph[cur.val].append(parent.val)
                graph[parent.val].append(cur.val)
            
            if cur.left:
                bind_node(cur.left, cur)
            if cur.right:
                bind_node(cur.right,cur)

        bind_node(root, None)
        visited = set([target.val])
        answer = []

        def bfs(target):
            q = deque([(target.val, 0)])
            
            while q:
                val, dist = q.popleft()
                if dist == k:
                    answer.append(val)
                    continue

                for next_val in graph[val]:
                    if next_val not in visited:
                        q.append((next_val, dist+1))
                        visited.add(next_val)

        bfs(target)

        return answer