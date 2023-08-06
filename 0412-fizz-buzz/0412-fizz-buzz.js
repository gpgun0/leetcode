/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    const result = Array(n).fill({ value: "" });

    result.forEach((el, i) => {
        let j = i+1;
        if (j % 3 === 0 && j % 5 === 0) result[i] = "FizzBuzz";
        else if (j % 3 === 0) result[i] = "Fizz";
        else if (j % 5 === 0) result[i] = "Buzz";
        else result[i] = String(j);
    })

    return result;
};