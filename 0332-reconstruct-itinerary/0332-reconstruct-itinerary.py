class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        result = []
        
        for from_, to_ in tickets:
            graph[from_].append(to_)
        
        for from_ in graph:
            graph[from_].sort()

        def dfs(from_):
            while graph[from_]:
                to_ = graph[from_].pop(0)
                dfs(to_)

            result.append(from_)

        dfs('JFK')
        return result[::-1]