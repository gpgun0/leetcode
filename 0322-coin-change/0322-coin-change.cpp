class Solution {
public:
    int n;
    int INF = 1e9;
    int coinChange(vector<int>& coins, int amount) {
        n = coins.size();
        vector<int> dp(amount+1, INF);
        dp[0] = 0;

        for (int coin: coins) {
            for (int i=coin; i<amount+1; i++) {
                dp[i] = min(dp[i-coin]+1, dp[i]);
            }
        }

        return dp[amount] == INF ? -1 : dp[amount];
    }
};