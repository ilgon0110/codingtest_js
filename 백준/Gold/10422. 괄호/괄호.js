let fs = require("fs");
let _ = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
let [N, ...arr] = _;

const solution = (arr) => {
  arr = arr.map(Number);
  let dp = Array.from({ length: 5001 }).fill(0n);

  dp[0] = 1n;
  dp[2] = 1n;
  for (let i = 4; i <= 5000; i += 2) {
    for (let j = 0; j <= i - 2; j += 2) {
      dp[i] += dp[j] * dp[i - 2 - j];
    }
    dp[i] %= 1000000007n;
  }

  dp = dp.map((v) => v.toString());

  for (let i of arr) {
    console.log(dp[i]);
  }
};

solution(arr);
