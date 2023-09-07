let fs = require("fs");
let _ = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

let [_N, ...arr] = _;

const [n, f] = _N.split(" ").map(Number);

function solution(n, f) {
  let answer;
  let arr = Array.from({ length: n }, (_, i) => i + 1);
  let visited = Array.from({ length: n }, () => 0);
  let tmp = [];
  function isCorrect(L, arr) {
    if (L === n - 1) {
      return arr.reduce((a, c) => a + c, 0) === f;
    } else {
      let tmp = [];
      for (let i = 0; i < arr.length - 1; i++) {
        tmp.push(arr[i] + arr[i + 1]);
      }
      return isCorrect(L + 1, tmp);
    }
  }
  let flag = 0;
  function DFS(L) {
    if (flag) return;
    if (L === n) {
      if (isCorrect(0, tmp)) {
        flag = 1;
        answer = tmp.slice().join(' ');
        return;
      }
      return;
    } else {
      for (let i = 0; i < arr.length; i++) {
        if (visited[i]) continue;
        visited[i] = 1;
        tmp.push(arr[i]);
        DFS(L + 1);
        visited[i] = 0;
        tmp.pop();
      }
    }
  }
  DFS(0);
  return answer;
}

console.log(solution(n, f));
