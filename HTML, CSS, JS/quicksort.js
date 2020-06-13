//Node.js 10.14.0
//Plain Javascript and Node.js is supported
// html/css is not supported here 

const quick = (array) => {
  if(array.length < 1) return [];
  
  let left = [];
  let right = [];
  let pivot = array[0];
  
  for(let i=1;i<array.length;i++){
    if(pivot > array[i]){
      left.push(array[i]);
    }else{
      right.push(array[i]);
    }
  }
  return [].concat(quick(left),pivot,quick(right));
};

console.log(quick([5,3,1,4,2]));
