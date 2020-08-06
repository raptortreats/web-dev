//arrays
//ordered collection of values
//list of commentsin insta and fb posts
//songs in a playlist
//creatin arrays
//arrays are indexed

//let numsArr = [1, 2, 3, 4, 5, 6];
//let emptyArr = [];
let colors = ["red", "blue", "green", "orange"]; //strings are indexed
//let mixedArr = ["hi", 23];

console.log(colors[2]);

//modifying the index
colors[2] = "white";
console.log(colors);
// array methods
//push--add new elements to end
colors.push("yellow");
console.log(colors);
//pop--remove from end
console.log(colors.pop());
//shift-- remove from start
colors.shift();
console.log(colors);
//unshift -- adds new element to start
colors.unshift("red");
console.log(colors);
//concat--merge arrays
let feeling = ["fav colours"];
let tot = colors.concat(feeling);
console.log(tot);
//includes--looks for a value
console.log(tot.includes("red"));
//indexOf--just like string indexOf
console.log(tot.indexOf("blue"));
//join--creates a str from an array
console.log(tot.join());
//reverse--to reverse an array
console.log(tot.reverse());
//slice--copy portion of an array
let furious = tot.slice(2);
console.log(furious);
//splice--remove or replace elements
tot.splice(2, 0, "yoyo");
console.log(tot);
//sort--sorts an array
console.log(tot.sort());
