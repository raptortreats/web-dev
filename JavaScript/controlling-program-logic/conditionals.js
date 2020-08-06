// conditionals

// IF
// ELSE
// ELSE IF

// let a = 10
// let b = 5
// if(a>b){
//     console.log("highest")
// }
// else if(a===b){
//     console.log("equal")
// }
// else{
//     console.log("lowest")
// }

var rating;

if (rating == 5) {
  console.log("super cool");
} else if (rating == 4) {
  console.log("cool");
} else if (rating == 3) {
  console.log("good");
} else if (rating == 2) {
  console.log("bad");
} else if (rating == 1) {
  console.log("worst");
} else console.log("not rated");

// password validator

// 1. password must contain atleast 6 characteristics long
// 2. password should not contain spaces
// 3. if password doesn't contain atleast 6 characteristics then print password should not be less than 6 characteristics
// 4. if password contains spaces then print password should not contain spaces
// 5. if password contains 6 characteristics and doesn't contain spaces then print valid password

// var password = "roiuijjch";
// if(password === undefined){
//     console.log('password shoudnt be blank')
// }else if(password.indexOf(" ")!== -1){
//     console.log("password should not contain spaces")
// }else if(password.length<6){
//     console.log("password shoudnt be less than 6 char")
// }
// else console.log("valid password")

// Truthy and Falsy values

// false
// 0
// null
// undefined
// NaN
// ""

// everything else is true

// logical operators
// AND (&&)
// OR (||)
// // NOT (!)

// let a = 12;
// let b= 45
// if(a===12 && b<50){
//     console.log("yes")
// }

console.log(1 <= 4 && "a" === "a");
console.log(23 === 25 && 45 === 45);
console.log(1 < 2 || 5 === 5);
console.log(!0);

//BO D M A S

//console.log(100/4*5+25-50)

//! has high precedence next && and ||
// ! > && > ||

// ternary operator

// condition ? expiftrue: expiffalse

let password = "ueiefj";

password === undefined
  ? console.log("passwrd shoudnt be blank")
  : console.log("valid");

let userstatus = "online";
userstatus === "online" ? console.log("green") : console.log("red");

let status = "offline";

let color = status === "offline" ? "red" : "green";
console.log(color);

// let variable;
// variable = "value";

// let a = 123;
// let b = a;
// let c = a * "abc";

// variables can't be declared using numbers
// variables can't start from capital letter instead use camelCasing
// variables can't be symbols or special characteristics

// let userstatus;
// let sriKalkiRochish;

// let a1;

// print only rochish from sri kalki rochish

let name = "sri kalki rochish";
console.log(name.split(10));
let firstName = name.split(" ");
console.log(firstName[2][1]);
