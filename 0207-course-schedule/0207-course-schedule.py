class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        
        for a, b in prerequisites:
            graph[a].append(b)

        visited = set()
        traced = set()

        def dfs(cur):
            if cur in visited:
                return True

            if cur in traced:
                return False
        
            traced.add(cur)

            for next_ in graph[cur]:
                if not dfs(next_):
                    return False
            
            traced.remove(cur)
            visited.add(cur)
            return True

        for x in list(graph):
            if not dfs(x):
                return False
        
        return True