type F = (...p: any[]) => any

function debounce(fn: F, t: number): F {
    let timeId = null;
    
    return function(...args) {
        const context = this;
        
        clearTimeout(timeId);
        timeId = setTimeout(() => {
            fn.apply(context, args);
        }, t)
    }
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */