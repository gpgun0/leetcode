class Solution {
public:
    char findTheDifference(string s, string t) {
        map<char, int> dict;
        char answer;

        for (auto c: s) {
            dict[c] += 1;
        }

        for (auto c: t) {
            if (dict[c]) {
                dict[c] -= 1;
            } else {
                answer = c;
                break;
            }
        }
        
        return answer;
    }
};