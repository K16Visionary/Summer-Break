// Unary operator increment and decrement

let a = 4;

console.log("Increment : ",a++); // here ++ means add the value by 1
console.log("Decrement : ",a--); // here -- means substract the value by 1

// In this two concept also come prefix and postfix
//Addition prefix
let b = 2
console.log("Addition prefix : ",++b); //first it will increase the value by 1 then print
console.log("prefix : ",++b);
//Addition postfix
let c = 6
console.log("Addition postfix : ",c++); //first it will print the value then increase by 1
console.log("postfix : ",c++);

//Substraction prefix
let d = 8
console.log("Substraction prefix : ",--d); //first it will decrease the value by 1 then print
console.log("prefix : ",--d);
//Substraction postfix
let e = 9
console.log("Substraction postfix : ",e--); //first it will print the value and then decrease the value by 1
console.log("postfix : ",e--);