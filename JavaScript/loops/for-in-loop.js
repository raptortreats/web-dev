// for in loop is used to iterate over objects

// let students = {
//   name: "rochish",
//   age: 23,
// };

// for (let student of Object.keys(students)) {
//   console.log(student);
// }

// for (let student in students) {
//   console.log(student);
// }

// rochish has walked 238 steps today and burnt 10000 calories and today his heartrate is 130

let fitBitData = {
  user1: { name: "rochish", steps: 238, calories: 10000, heartrate: 130 },
  user2: { name: "ravi", steps: 238999, calories: 1000, heartrate: 130 },
  user3: { name: "santosh", steps: 2389945, calories: 100, heartrate: 130 },
  user4: { name: "krishna", steps: 238599, calories: 1, heartrate: 130 },
  user5: { name: "pdvp", steps: 239, calories: 100, heartrate: 130 },
  user6: { name: "chandana", steps: 238999, calories: 10000, heartrate: 130 },
};

for (data in fitBitData) {
  let user = fitBitData[data];
  console.log(
    `${user.name} has walked ${user.steps} today and burnt ${user.calories} and today his heartrate is ${user.heartrate}`
  );
}
