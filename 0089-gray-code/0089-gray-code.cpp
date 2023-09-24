class Solution {
public:
    map<int, int> bitsMap;
    vector<int> answer = {0};
    set<int> seen;

    int getOnCount() {
        int count = 0;
        for (auto iter=bitsMap.begin(); iter!=bitsMap.end(); iter++) {
            if (iter->second) {
                count++;
            }
        }

        return count;
    }

    bool backtrack(int num, int n) {
        if (num < 0 || num >= pow(2, n)) {
            return false;
        }

        if (answer.size() == pow(2, n)) {
            // if (getOnCount() == 1) {
                return true;
            // }
            // return false;
        }

        int nextNum = 0;
        bool flag = false;

        for (int i=0; i<n; i++) {
            if (bitsMap[pow(2, i)]) {
                nextNum = num - pow(2, i);
            } else {
                nextNum = num + pow(2, i);
            }
            bitsMap[pow(2, i)] ^= 1;

            if (seen.count(nextNum)) {
                bitsMap[pow(2, i)] ^= 1;
                continue;
            }

            seen.insert(nextNum);
            answer.push_back(nextNum);

            flag = backtrack(nextNum, n);
            if (flag) {
                return true;
            }

            answer.pop_back();
            seen.erase(nextNum);

            bitsMap[pow(2, i)] ^= 1;
        }

        return flag;
    }

    vector<int> grayCode(int n) {
        for (int i=0; i<n; i++) {
            bitsMap[pow(2, i)] = 0;
        }

        seen.insert(0);
        backtrack(0, n);

        return answer;
    }
};