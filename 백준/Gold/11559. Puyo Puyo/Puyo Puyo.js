let fs = require("fs");
let _ = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

let [...arr] = _;
const input = arr.map((v) => v.split(" ").map((el) => el.split(""))).flat();
const N = 12;
const M = 6;

// const test = [
//   [".", ".", ".", ".", ".", "."],
//   [".", ".", ".", ".", ".", "."],
//   [".", ".", ".", ".", ".", "."],
//   [".", ".", ".", ".", ".", "."],
//   [".", ".", ".", ".", ".", "."],
//   [".", ".", ".", ".", ".", "."],
//   [".", ".", ".", ".", ".", "."],
//   [".", ".", ".", ".", ".", "."],
//   [".", ".", ".", ".", ".", "."],
//   [".", ".", ".", ".", ".", "."],
//   [".", ".", ".", "G", ".", "."],
//   [".", ".", "G", "G", "G", "."],
// ];

// console.log(isNoMorePuyo(test));

function isPuyo(pos, board) {
  const copyArr = [];
  board.forEach((v) => copyArr.push([...v]));
  const dx = [-1, 0, 1, 0];
  const dy = [0, -1, 0, 1];
  const queue = [pos];
  const tracking = [pos];
  let cnt = 0;
  const visited = Array.from({ length: N }, () =>
    Array.from({ length: M }).fill(0)
  );
  visited[pos[0]][pos[1]] = 1;
  while (queue.length) {
    let [x, y] = queue.shift();
    for (let i = 0; i < 4; i++) {
      let nx = x + dx[i];
      let ny = y + dy[i];
      if (nx < 0 || nx >= N || ny < 0 || ny >= M || visited[nx][ny] > 0)
        continue;
      if (copyArr[nx][ny] === copyArr[x][y]) {
        visited[nx][ny] = 1;
        queue.push([nx, ny]);
        tracking.push([nx, ny]);
        cnt++;
      }
    }
  }
  if (cnt < 3) return false;
  return turnPuyo(tracking, copyArr);
}

function turnPuyo(tracking, board) {
  for (let [x, y] of tracking) {
    board[x][y] = ".";
  }
  return board;
}

function goDown(board) {
  board = rotate(board);
  let now = [];
  board.forEach((v) => {
    now.push(v.filter((el) => el !== "."));
  });
  now.forEach((el) => {
    el.reverse();
    while (el.length < N) {
      el.push(".");
    }
    el.reverse();
  });
  return rotate(now);
}

function rotate(board) {
  let newBoard = Array.from({ length: board[0].length }, () =>
    Array.from({ length: board.length }).fill(0)
  );

  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[0].length; j++) {
      newBoard[j][i] = board[i][j];
    }
  }
  return newBoard;
}

function isNoMorePuyo(board) {
  const copyArr = [];
  board.forEach((v) => copyArr.push([...v]));
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (copyArr[i][j] !== ".") {
        if (isPuyo([i, j], copyArr).length > 0) return false;
      }
    }
  }
  return true;
}

function copyArray(arr) {
  let newArr = [];
  arr.forEach((v) => newArr.push([...v]));
  return newArr;
}

let flag = false;
function DFS(L, arr) {
  if (flag) return;
  if (isNoMorePuyo(arr)) {
    console.log(L);
    flag = true;
    return;
  } else {
    let copyArr = copyArray(arr);
    for (let i = 0; i < N; i++) {
      for (let j = 0; j < M; j++) {
        if (copyArr[i][j] !== ".") {
          const result = isPuyo([i, j], copyArr);
          if (result.length > 0) {
            copyArr = isPuyo([i, j], copyArr);
          }
        }
      }
    }
    DFS(L + 1, goDown(copyArr));
  }
}
DFS(0, input);
