const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('String: ', input => {
  input = input.trim();
  let output = '';
  Array.prototype.forEach.call(input, letter => {
    const code = letter.charCodeAt();
    const bin = code.toString(2);
    
    console.log(`${letter} -> ${code} -> ${bin}`);
    
    output += bin + ' ';
  });
  console.log('---------------------------');
  console.log(output);
  rl.close();
});
