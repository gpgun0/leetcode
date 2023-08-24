class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = int(1e9)

        graph = defaultdict(list)

        for a, b, cost in times:
            graph[a].append((cost, b))
        
        visited = set()
        costs = [INF]*(n+1)

        def dijkstra(start):
            q = [(0, start)]
            costs[start] = 0

            while q:
                cost, cur = heappop(q)

                for nxt in graph[cur]:
                    nxt_cost, nxt_node = nxt
                    if costs[nxt_node] > cost + nxt_cost:
                        costs[nxt_node] = cost + nxt_cost
                        heappush(q, (costs[nxt_node], nxt_node))

        dijkstra(k)

        if INF in costs[1:]:
            return -1
        return max(costs[1:])