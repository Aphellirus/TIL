let count = 1;
const hackIt = setInterval(() => {
console.log(`Hacking ${count * 10}%`);
if (count === 10) {
console.log('Hacked Successfully!!');
clearInterval(hackIt);
}
else count++
}, 1000);
