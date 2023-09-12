class Solution {
public:
    int strStr(string haystack, string needle) {
        int n = haystack.length();
        int m = needle.length();

        for (int startIndex=0; startIndex<=n-m; startIndex++) {
            for (int i=0; i<m; i++) {
                if (haystack[i+startIndex] != needle[i]) {
                    break;
                }

                if (i == m-1) {
                    return startIndex;
                }
            }
        }

        return -1;
    }
};