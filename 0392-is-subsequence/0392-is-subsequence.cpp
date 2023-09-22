class Solution {
public:
    bool isSubsequence(string s, string t) {
        int p = 0;

        for (int i=0; i<t.length(); i++) {
            if (t[i] == s[p]) {
                p += 1;
            }
        }

        if (p == s.length()) {
            return true;
        }

        return false;        
    }
};