/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    return Array.from({ length: n }, (_, i) => {
        i += 1;

        return (i % 3 === 0 && i % 5 === 0) ? "FizzBuzz"
            : (i % 3 === 0) ? "Fizz"
            : (i % 5 === 0) ? "Buzz"
            : "" + i;
    });
};