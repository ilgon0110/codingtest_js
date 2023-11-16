let fs = require("fs");
let _ = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

let [input, ...arr] = _;

const [N, M] = input.split(" ").map(Number);
const board = arr.map((v) => v.split(" ").map(Number));

function chickenDist(pos1, pos2) {
  const [r1, c1] = pos1;
  const [r2, c2] = pos2;
  return Math.abs(r1 - r2) + Math.abs(c1 - c2);
}

let chickens = [];
let homes = [];
for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    if (board[i][j] === 1) {
      homes.push([i, j]);
    }
    if (board[i][j] === 2) {
      chickens.push([i, j]);
    }
  }
}

let answer = Number.MAX_SAFE_INTEGER;

const result = getCombinations(chickens, M);
result.forEach((chicken) => {
  let sum = 0;
  for (let home of homes) {
    let tmp3 = [];
    chicken.forEach((c) => tmp3.push(chickenDist(c, home)));
    const nearDist = Math.min(...tmp3);
    sum += nearDist;
  }
  answer = Math.min(answer, sum);
});
console.log(answer);

function getCombinations(arr, select) {
  const results = [];
  if (select === 1) return arr.map((e) => [e]);
  arr.forEach((e, i, o) => {
    const rest = o.slice(i + 1);
    const combinations = getCombinations(rest, select - 1);
    const attached = combinations.map((r) => [e, ...r]);
    results.push(...attached);
  });

  return results;
}

