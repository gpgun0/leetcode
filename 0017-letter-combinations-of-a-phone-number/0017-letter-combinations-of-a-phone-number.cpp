class Solution {
public:
    vector<string> answer;
    map<char, string> dict = {
        {'2', "abc"},
        {'3', "def"},
        {'4', "ghi"},
        {'5', "jkl"},
        {'6', "mno"},
        {'7', "pqrs"},
        {'8', "tuv"},
        {'9', "wxyz"}
    };

    void backtrack(string path, string digits, int idx, int n) {
        if (idx == n && path != "") {
            answer.push_back(path);
            return;
        }

        for (auto c: dict[ digits[idx] ]) {
            backtrack(path+c, digits, idx+1, n);
        }
        return;
    }

    vector<string> letterCombinations(string digits) {
        int n = digits.length();
        backtrack("", digits, 0, n);

        return answer;
    }
};