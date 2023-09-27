class Solution {
public:
    vector<string> answer;

    void backtrack(int nth, int lastIdx, string ip, string substr, string s, int n) {
        if (substr.length() > 1 && substr[0] == '0') {
            return;
        }
        if (substr != "" && stoi(substr) > 255) {
            return;
        }

        if (nth == 4 && lastIdx != n-1) {
            return;
        }

        if (nth <= 1) {
            ip += substr;
        } else {
            ip += "." + substr;
        }

        if (nth == 4) {
            answer.push_back(ip);
            return;
        }

        string nxtSubstr = "";

        for (int i=lastIdx+1; i<min(n, lastIdx+4); i++) {
            nxtSubstr += s[i];
            backtrack(nth+1, i, ip, nxtSubstr, s, n);
        }

        return;
    }

    vector<string> restoreIpAddresses(string s) {
        int n = s.length();
        if (n > 12) {
            return {};
        }

        backtrack(0, -1, "", "", s, n);

        return answer;
    }
};