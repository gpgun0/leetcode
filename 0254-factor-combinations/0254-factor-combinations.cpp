class Solution {
public:
    vector<vector<int>> answer;

    void backtrack(vector<int>& path, int num, int n) {
        if (num == 1) {
            answer.push_back(path);
            return;
        }

        int s = 2;
        if (!path.empty()) {
            s = path[path.size()-1];
        }

        for (int i=s; i<=num; i++) {
            if (i != n && num % i == 0) {
                path.push_back(i);
                backtrack(path, num/i, n);
                path.pop_back();
            }
        }

        return;
    }

    vector<vector<int>> getFactors(int n) {
        vector<int> path = {};

        if (n == 1) {
            return answer;
        }
        backtrack(path, n, n);

        return answer;
    }
};