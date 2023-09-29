class Solution {
public:
    vector<string> answer;
    map<char, vector<char>> dict = {
        {'2', {'a', 'b', 'c'}},
        {'3', {'d', 'e', 'f'}},
        {'4', {'g', 'h', 'i'}},
        {'5', {'j', 'k', 'l'}},
        {'6', {'m', 'n', 'o'}},
        {'7', {'p', 'q', 'r', 's'}},
        {'8', {'t', 'u', 'v'}},
        {'9', {'w', 'x', 'y', 'z'}}
    };

    void backtrack(string path, string digits, int idx, int n) {
        if (path.length() == n) {
            if (path == "") {
                return;
            }
            answer.push_back(path);
            return;
        }

        char key = digits[idx];

        for (auto c: dict[key]) {
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