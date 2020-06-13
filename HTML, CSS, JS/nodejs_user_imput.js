//Node.js 10.14.0
//Plain Javascript and Node.js is supported
// html/css is not supported here 

const getInput = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

getInput.question('Who are you?', name => {
    console.log(`Hey there ${name}!`);
    print('Have a good day, ' + name)
    
    getInput.close();
    process.exit();
});


function print(string){
    console.log(string)
}
