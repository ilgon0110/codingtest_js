let fs = require("fs");
let _ = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

let [_N, ...arr] = _;

const [N, M] = _N.split(" ");
arr = arr.map((v) => v.split(" ").map(Number));

let dx = [-1, 0, 1, 0];
let dy = [0, -1, 0, 1];
let count = 0;
let answer = 0;
let ans = [];
for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    if (arr[i][j]) {
      let queue = [];
      let cnt = 0;
      arr[i][j] = 0;
      count++;
      queue.push([i, j]);
      while (queue.length) {
        cnt++;
        let [x, y] = queue.shift();
        for (let k = 0; k < 4; k++) {
          let nx = dx[k] + x;
          let ny = dy[k] + y;
          if (nx >= 0 && nx < N && ny >= 0 && ny < M) {
            if (arr[nx][ny]) {
              arr[nx][ny] = 0;
              queue.push([nx, ny]);
            }
          }
        }
      }
      answer = Math.max(answer, cnt);
    }
  }
}
ans.push(count, answer);
ans.forEach((v) => console.log(v));
