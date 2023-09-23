class Solution {
public:
    vector<string> answer;
    void backtrack(string path, int a, int b, int n) {
        if (path.length() == n*2) {
            answer.push_back(path);
            return;
        }

        if (a == n) {
            backtrack(path + ")", a, b+1, n);
        }
        else if (a == b) {
            backtrack(path + "(", a+1, b, n);
        }
        else {
            backtrack(path + "(", a+1, b, n);
            backtrack(path + ")", a, b+1, n);
        }

        return;
    }

    vector<string> generateParenthesis(int n) {
        backtrack("", 0, 0, n);

        return answer;
    }
};