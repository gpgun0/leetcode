class Solution {
public:
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        vector<int> answer;
        priority_queue<pair<int, int>> pq;
        int m = mat.size();
        int n = mat[0].size();

        for (int i=0; i<m; i++) {
            int j=0;
            for (j=0; j<n; j++) {
                if (mat[i][j] == 0) {
                    break;
                }
            }
            pq.push(make_pair(-(j-1), -i));
        }
        
        while (k--) {
            pair<int, int> p = pq.top();
            pq.pop();
            answer.push_back(-p.second);
        }

        return answer;
    }
};