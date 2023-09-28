class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> answer = {0};
        
        for (int i=1; i<n+1; i++) {
            int mask = 1 << (i-1);
            for (int j=answer.size()-1; j>=0; j--) {
                answer.push_back(answer[j] | mask);
            }
        }

        return answer;
    }
};