class Solution {
public:

    string commonPrefix(string left, string right) {
        int m = min(left.length(), right.length());
        for (int i=0; i<m; i++) {
            if (left[i] != right[i]) {
                return left.substr(0, i);
            }
        }
        return left.substr(0, m);
    }
    string longestCommonPrefix(vector<string>& strs, int l, int r) {
        if (l == r) {
            return strs[l];
        }

        int mid = (l+r)/2;
        string leftStr = longestCommonPrefix(strs, l, mid);
        string rightStr = longestCommonPrefix(strs, mid+1, r);
        
        return commonPrefix(leftStr, rightStr);
    }

    string longestCommonPrefix(vector<string>& strs) {
        return longestCommonPrefix(strs, 0, strs.size()-1);
    }
};