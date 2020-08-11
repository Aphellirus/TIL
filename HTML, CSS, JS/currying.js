// Javascript currying
// This is punk! 

// Simple example
const add = (a) => (b) => a+b;

console.log([1,2,3].map(add(3)));
console.log(add(3)(3));

// more complicated
// note this checks if b is greater than a.
// this might seem counter intuitive but read it aloud,
// and it will make sense.
// gt(3)(4)
// first gt(3) makes a function that checks if a number
// is greater than 3
// then that function is called with 4
const gt = (a) => (b) => b > a;

console.log([1,2,3,4,5].filter(gt(3)));

// complex example
const lt = (a) => (b) => b < a;
const orFunc = (a) => (b) => (c) => b(c) || a(c);

console.log([1,2,3,4,5,6,7].filter(orFunc(gt(4))(lt(2))))
