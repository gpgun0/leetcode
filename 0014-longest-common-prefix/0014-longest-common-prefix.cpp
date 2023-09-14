class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string prev = strs[0];

        for (int i=1; i<strs.size(); i++) {
            string cur = strs[i];
            int n = min(prev.length(), cur.length());
            int j=0;
            for (j=0; j<n; j++) {
                if (prev[j] != cur[j]) {
                    break;
                }
            }
            prev = prev.substr(0, j);
        }

        return prev;
    }
};