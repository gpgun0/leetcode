class Solution {
public:
    int n;
    int INF = 1e9;
    int answer;

    int dfs(vector<int>& coins, int amount, vector<int>& mem) {
        int min_cost = INF;

        if (amount == 0) {
            return 0;
        }

        if (mem[amount]) {
            return mem[amount];
        }

        for (int coin: coins) {
            if (amount-coin < 0) {
                continue;
            }
            
            min_cost = min(dfs(coins, amount-coin, mem)+1, min_cost);
        }

        mem[amount] = min_cost;
        return mem[amount];
    }


    int coinChange(vector<int>& coins, int amount) {
        n = coins.size();
        vector<int> mem(amount+1, 0);
        answer = dfs(coins, amount, mem);

        return answer == INF ? -1 : answer;
    }
};