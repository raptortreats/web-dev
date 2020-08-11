// for...of loop is used to iterate over arrays

let nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// for (let i = 0; i < nums.length; i++) {
//   console.log(nums[i]);
// }

// for (let num of nums) {
//   if (num % 2 === 0) {
//     console.log(num);
//   }
// }

for (let num of nums) {
  console.log(`2 x ${num} = ${2 * num}`);
}
