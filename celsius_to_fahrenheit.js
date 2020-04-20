//const module_deg = require("./module_deg");
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

var degree = function(celcius){
  var f;
  var result;
  f = (1.8 * celcius) + 32;
  return result = f;
  console.log("Fahrenheit = " + result)
}

rl.question("Input your degree in Celcius here = ", function(celc) {
  console.log(`Celcius = ${celc}`);
  console.log("Fahrenheit = " + degree(celc));
  //degree.emit("degreenih", celc);
  rl.close();
});

rl.on("close", function() {
    console.log("\nBYE BYE !!!");
    process.exit(0);
});