/**
 * @param {number} init
 * @return {{ increment: Function, decrement: Function, reset: Function }}
 */
var createCounter = function(init) {
    let current = init;

    const increment = () => ++current;
    const decrement = () => --current;
    const reset = () => current = init;

    return {
        increment,
        decrement,
        reset
    };
};
