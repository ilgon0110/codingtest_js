let fs = require("fs");
let _ = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

let [N, ...arr] = _;

let [n, v] = N.split(" ").map(Number);
arr = arr.map((v) => v.split(" ").map(Number));

function countConnectedComponents(N, edges) {
  const graph = new Array(N).fill(null).map(() => []);
  const visited = new Array(N).fill(false);

  function dfs(node) {
    visited[node] = true;
    for (let neighbor of graph[node]) {
      if (!visited[neighbor]) {
        dfs(neighbor);
      }
    }
  }

  for (let edge of edges) {
    const [u, v] = edge;
    graph[u - 1].push(v - 1);
    graph[v - 1].push(u - 1);
  }

  let components = 0;
  for (let i = 0; i < N; i++) {
    if (!visited[i]) {
      dfs(i);
      components++;
    }
  }

  return components;
}

console.log(countConnectedComponents(n, arr));
