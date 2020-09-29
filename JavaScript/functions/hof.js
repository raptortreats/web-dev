//func that operate on or with other functions
//1-accept other func as arg
//2-return a function

function callTwice(func) {
  func();
  func();
}

function laugh() {
  console.log("hihihihi");
}

callTwice(laugh);

function greet(name) {
  let name = function () {};
}
