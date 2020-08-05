var name = "rochish"

var len = name.length

console.log(len)

// todays assignment

// indexOf()
var dog = [1,2,3,4,5];
console.log(dog.indexOf(3))

// lastIndexOf()
console.log(dog.lastIndexOf(4))

// search() -- to know the position
var mynote = "i will never give up"
console.log(mynote.search("never"))
// slice(start, end) cuts the part of a string and gives the o/p
console.log(mynote.slice(11,14))
// substring(start, end)--its simiar to slice but dont accept negative indexes
console.log(mynote.substring(15,16))

// substr(start, length) this slices out the rest of the string
console.log(mynote.substr(6))
// replace() this replaces the specified value with another value
var lappy = "i have a macbook"
console.log(lappy.replace("macbook", "lenovo"))
// toUpperCase()
var cat = "pussy"
console.log(cat.toUpperCase())
// toLowerCase()
console.log(cat.toLowerCase())
// concat() this is used for joinig strings
var m = "i am naruto"
console.log(m.concat("uzumaki"))
// trim() this is used to remove the whitespace from a string
var n = "       hahahah"
console.log(n.trim())

// sup() converts the string into super script text
console.log(m.sup())
// repeat() this is used to repeat a string
var q = "moon"
console.log(q.repeat(2))
// includes() determines the string contains the character specified
console.log(m.includes("am"))
// bold() displays the text in bold
console.log(m.bold())
// fixed() displays the text as teletype text
console.log(m.fixed())

var arr = [1,2,3,3,4,5,6]
        // 0 1 2 3 4 5 6
console.log(arr.indexOf(2))
console.log(arr.lastIndexOf(3))

// quiz

// what is the value of age
//54

const age = "5" + "4"

console.log(age)

// what does this evalueate to?
//i

console.log("pecan pie"[7])

// what is the value of song?
//LONDON CALLING

let song = "london calling";

console.log(song.toUpperCase())

// what is the value of cleanedInput?
//rochish@gmail.com

let userInput = "        Rochish@gmail.com";
let cleanedInput = userInput.trim().toLowerCase();
console.log(cleanedInput)

// what is the value of index?
//0

let park = 'huda park';
const index = park.indexOf('huda');
console.log(index);

