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

if(rating == 5) {
    console.log("super cool")
} else if(rating == 4) {
    console.log("cool")
} else if(rating == 3){
    console.log("good")
} else if(rating == 2){
    console.log("bad")
} else if(rating == 1){
    console.log("worst")
} else console.log("not rated")

// password validator

// 1. password must contain atleast 6 characteristics long
// 2. password should not contain spaces
// 3. if password doesn't contain atleast 6 characteristics then print password should not be less than 6 characteristics
// 4. if password contains spaces then print password should not contain spaces
// 5. if password contains 6 characteristics and doesn't contain spaces then print valid password

var password;
if(password == undefined){
    console.log('password shoudnt be blank')
}else if(password.includes(" ")){
    console.log("password should not contain spaces")
}else if(password.length<6){
    console.log("password shoudnt be less than 6 char")
}
else console.log("valid password")