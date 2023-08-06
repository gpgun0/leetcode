/**
 * @param {number} num
 * @return {number}
 */
var numberOfSteps = function(num) {
    let result = 0;

    while (num) {
        if (num % 2 === 0) {
            num /= 2;
        } else {
            num -= 1;
        }
        result += 1;
    }

    return result;
};