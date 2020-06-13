//Node.js 10.14.0
//Plain Javascript and Node.js is supported
// html/css is not supported here

var countFrom = 20
var counter = setInterval(() => {
  if (countFrom >= 0) {
    console.log(countFrom--)
  } else {
    clearInterval(counter)
    console.log('boom!!')
    }
}, 1000);
