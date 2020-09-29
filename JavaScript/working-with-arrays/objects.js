// objects

// objects are collections of properties
// properties are a key-value pairs

// rather than accessing data using an index, we use custom keys

const fitBitData = {
  totalSteps: 123456,
  totalMiles: 1234,
  heartRate: 30,
  calories: 10000,
};

const post = {
  comment: "arey nee mokam eppudaina addam lo chusukunnava?",
  likes: 0,
  share: 4,
};

const school = {
  student1: {
    name: "rochish",
    age: 23,
    class: "ukg",
    rank: "topper",
  },
  student2: {
    name: "ravi",
    age: 23,
    class: "ukg",
    rank: "3rd",
  },
};
school.student1["class"] = "1st class";
console.log(school.student1);
school.student1["sports"] = "pubg";
console.log(school);
