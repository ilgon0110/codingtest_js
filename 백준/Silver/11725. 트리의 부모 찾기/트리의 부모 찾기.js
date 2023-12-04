let fs = require("fs");
let _ = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

let [N, ...arr] = _;
N = Number(N);
arr = arr.map((v) => v.split(" ").map(Number));

const graph = Array.from({ length: N + 1 }, () => []);
const visited = Array.from({ length: N + 1 }).fill(0);
const head = Array.from({ length: N + 1 }, () => 0);
for (let [a, b] of arr) {
  graph[a].push(b);
  graph[b].push(a);
}

function DFS(node, s) {
  if (s === N) {
    return;
  } else {
    for (let next of graph[node]) {
      if (visited[next]) continue;
      visited[next] = 1;
      head[next] = node;
      DFS(next, s + 1);
    }
  }
}

DFS(1, 0);
let answer = "";
for (let i = 2; i < head.length; i++) {
  answer += head[i] + "\n";
}

console.log(answer);
