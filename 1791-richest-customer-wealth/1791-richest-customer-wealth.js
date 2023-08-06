/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function(accounts) {
    let result = 0;

    accounts.forEach((account, i) => {
        const sum = account.reduce((a, c) => a + c);

        result = Math.max(result, sum);
    })

    return result;
};