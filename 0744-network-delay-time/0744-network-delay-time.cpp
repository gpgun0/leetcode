class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        int INF = 2e9;
        vector<pair<int, int>> graph[n+1];
        priority_queue<pair<int, int>> q;
        vector<int> distances(n+1, INF);

        distances[k] = 0;
        q.push(make_pair(0, k));

        for (auto time: times) {
            int u = time[0], v = time[1], cost = time[2];
            graph[u].push_back(make_pair(v, cost));
        }

        while (!q.empty()) {
            int cost = -q.top().first, curNode = q.top().second;
            q.pop();

            if (distances[curNode] < cost) {
                continue;
            }

            for (auto next: graph[curNode]) {
                int nextNode = next.first, nextCost = next.second;

                if (distances[nextNode] > cost + nextCost) {
                    distances[nextNode] = cost + nextCost;
                    q.push(make_pair(-distances[nextNode], nextNode));
                }
            }
        }

        int answer = -1;
        for (int i=1; i<n+1; i++) {
            answer = max(distances[i], answer);
        }
        return answer == INF ? -1 : answer;
    }
};