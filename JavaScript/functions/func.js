function greet() {
  for (let i = 0; i < 10; i++) {
    console.log("hello");
  }
}
greet();

// functions with arguments

function squareOfNum(x) {
  console.log(x ** 2);
}

squareOfNum(350);

function greet1(name) {
  for (let i = 0; i < 10; i++) {
    console.log(`hello ${name}`);
  }
}
greet1("rochish");

// functions with multiple arguments

function add(a, b, c) {
  console.log(a + b + c);
}
add(1, 6, 8);

function avg(x, y, z, m) {
  console.log((x + y + z + m) / 4);
}
avg(2, 4, 6, 7);

function avg1(x, y, z, m) {
  return (x + y + z + m) / 4;
  console.log("hello");
}
console.log(avg1(2, 4, 6, 7));

// write a function passwordValidator which haas 2 arguments user and password
//passwword len shouldnt be less than 8 char
//shouldnt contain space
//user name shoudnt be empty
//if the conditions are true print valid password and username else print invalid

function pWuserValidator(user, password) {
  user === undefined && password === undefined
    ? console.log("user and pw shouldnt be blank")
    : console.log("valid");
  user.includes(" ") || password.includes(" ")
    ? console.log("both shoudnt contain spaces")
    : console.log("valid");
  password.length < 8
    ? console.log("shouldnt be lesss than 8 char")
    : console.log("valid");
}

pWuserValidator("qoiewww", "oqwhd");
//write a func for dice guessing game
function guesingame(guess) {
  const dice = Math.floor(Math.random() * 6) + 1;
  console.log(dice);
  console.log(guess);

  if (dice === guess) {
    return true;
  }
  return false;
}

console.log(guesingame(6));

// pangram - sentence which contains all the 26 alphabets
// function pangram(sent) {
//   const yo = ["abcdefghijklmnopqrstuvwxyz"];

//   sent.includes(yo.join(""))
//     ? console.log("a pangram")
//     : console.log("it isnt");
// }

// pangram("Pack my box with five dozen liquor jugs");
// write a function for pangram whether the given string contains all the alphabets print true if not false

// write a function which checks whether the given string is palindrome or not , if the given string is palindrome return true else return false
function palindrome(str) {
  a = str.split("").reverse().join("");
  if (str === a) {
    console.log("a palindrome");
  } else console.log("not a pal");
}

palindrome("romeo");
// examples of palindrome
// madam
// racecar
// level
// radar
// civic
// reviver

// password validator
// dice guessing
// pangram
// palindrome

// pangram

function isPangram(str) {
  let lowerCased = str.toLowerCase();
  for (let char of "abcdefghijklmnopqrstuvwxyz") {
    //console.log(lowerCased.indexOf(char));
    if (lowerCased.indexOf(char) === -1) {
      return false;
    }
  }
  return true;
}
console.log(isPangram("Pack my box with five dozen liquor jugs"));

function guessGame(user) {
  let computer = Math.floor(Math.random() * 6) + 1;
  if (user === computer) {
    return "user won";
  }
  return "user lost";
}

console.log(guessGame(5));

function fact(n) {
  f = 1;
  for (i = 1; i <= n; i++) {
    f = f * i;
  }
  console.log(f);
}

fact(6);
