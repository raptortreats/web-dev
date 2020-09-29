//variable visibility
//the location where a variable is defined as where we have access to that variable

// function helpMe() {
//   var msg = "help help help help help";
//   console.log(msg);
// }
// console.log(msg);
// helpMe();

// let msg = "help";
// function helpMe() {
//   let msg = "i'm safe";
//   console.log(msg);
// }
// helpMe();
// console.log(msg);

// let radius = 5;

// if (radius > 0) {
//   const PI = 3.141;
//   let circumference = 2 * PI * radius;
// }
// console.log(radius);
// console.log(PI); // not defined
// console.log(circumference); // not defined

// because PI and circumference are block scoped

function flower() {
  let name1 = "banthi puvvu";
  function name() {
    console.log(`rochish gadi chevilo ${name1}`);
  }
  name();
}

flower();

// with respect to flower function name1 is locally scoped
// with respect to name function name1 is globally scoped

function outer() {
  let hero = "krishna";
  function inner() {
    let cryForHelp = `${hero}, please fuck me!`;
    console.log(cryForHelp);
  }
  inner();
}

outer();

if (true) {
  var animal = "rochish";
  console.log(animal);
}

console.log(animal);
