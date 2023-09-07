let fs = require("fs");
let _ = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

let [_N, ...arr] = _;

const [N, M] = _N.split(" ");
arr = arr.map((v) => v.split("").map(Number));
let dx = [-1, 0, 1, 0];
let dy = [0, -1, 0, 1];

let queue = [];
let dist = Array.from({ length: N }, () => Array.from({ length: M }).fill(1));
arr[0][0] = 0;
queue.push([0, 0]);

while (queue.length) {
  let [x, y] = queue.shift();
  if (x === N - 1 && y === M - 1) {
    break;
  }
  for (let i = 0; i < 4; i++) {
    let nx = dx[i] + x;
    let ny = dy[i] + y;
    if (nx >= 0 && nx < N && ny >= 0 && ny < M && arr[nx][ny]) {
      arr[nx][ny] = 0;
      dist[nx][ny] = dist[x][y] + 1;
      queue.push([nx, ny]);
    }
  }
}
console.log(dist[N - 1][M - 1]);
