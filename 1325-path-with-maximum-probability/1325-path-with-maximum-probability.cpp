class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start_node, int end_node) {
        vector<double> probs(n, 0);
        vector<pair<int, double>> graph[n];
        priority_queue<pair<double, int>> pq;

        probs[start_node] = 1.0;
        pq.push(make_pair(1.0, start_node));

        for (int i=0; i<edges.size(); i++) {
            vector<int> edge = edges[i];
            int u = edge[0], v = edge[1];

            graph[u].push_back(make_pair(v, succProb[i]));
            graph[v].push_back(make_pair(u, succProb[i]));
        }

        while (!pq.empty()) {
            double prob = pq.top().first;
            int curNode = pq.top().second;
            pq.pop();

            if (probs[curNode] > prob) {
                continue;
            }

            for (auto next: graph[curNode]) {
                int nextNode = next.first;
                double nextProb = next.second;

                if (prob * nextProb > probs[nextNode]) {
                    probs[nextNode] = prob * nextProb;
                    pq.push(make_pair(prob * nextProb, nextNode));
                }
            }
        }


        return probs[end_node];
    }
};