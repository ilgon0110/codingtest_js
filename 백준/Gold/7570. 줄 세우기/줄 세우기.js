let fs = require("fs");
let _ = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

let [_N, ...arr] = _;
const N = Number(_N);
arr = arr.map((v) => v.split(" ").map(Number)).flat();

const dp = Array.from({ length: N + 1 }, () => 0);
let max = 0;
for (let i = 1; i <= N; i++) {
  const num = arr[i - 1];
  dp[num] = dp[num - 1] + 1;
  max = Math.max(dp[num], max);
}

console.log(N - max);
