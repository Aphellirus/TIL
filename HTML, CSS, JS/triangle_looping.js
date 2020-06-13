//Node.js 10.14.0
//Plain Javascript and Node.js is supported
// html/css is not supported here 

console.log("With for loop:");
var x = "";
for (let i = 1; i <= 7; i++) {
  x += "#";
  console.log(x);
}

console.log("");

console.log("With while loop");
var y = "";
var count = 1;
while (count <= 7) {
  y += "#";
  console.log(y);
  count++;
}
