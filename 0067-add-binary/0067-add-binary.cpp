class Solution {
public:
    string addBinary(string a, string b) {
        string answer = "";
        int carry = 0;
        int n = max(a.length(), b.length());
        a = string(n - a.length(), '0') + a;
        b = string(n - b.length(), '0') + b;

        for (int i=n-1; i>=0; i--) {
            if (a[i] == '1') {
                carry++;
            }
            if (b[i] == '1') {
                carry++;
            }

            if (carry%2 == 1) {
                answer += '1';
            } else {
                answer += '0';
            }

            carry /= 2;
        }
        if (carry == 1) {
            answer += '1';
        }
        reverse(answer.begin(), answer.end());
        return answer;
    }
};