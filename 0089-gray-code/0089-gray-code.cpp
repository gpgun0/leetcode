class Solution {
public:
    map<int, int> bitsMap;
    vector<int> answer = {0};
    set<int> seen;

    bool backtrack(int num, int n) {
        if (answer.size() == pow(2, n)) {
            return true;
        }

        for (int i=0; i<n; i++) {
            int nextNum = num ^ (1 << i);

            if (seen.count(nextNum)) {
                continue;
            }

            seen.insert(nextNum);
            answer.push_back(nextNum);

            if (backtrack(nextNum, n)) {
                return true;
            }

            answer.pop_back();
            seen.erase(nextNum);
        }

        return false;
    }

    vector<int> grayCode(int n) {
        seen.insert(0);
        backtrack(0, n);

        return answer;
    }
};