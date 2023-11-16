let fs = require("fs");
let _ = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

let [input, ...arr] = _;

input = Number(input);
arr = arr.map((v) => v.split(" ").map(Number));

let N = arr.length;

const rotate = (board) => {
  let newBoard = Array.from(Array(N), () => Array(N).fill(0));
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      newBoard[j][i] = board[i][j];
    }
  }
  return newBoard;
};

const goUp = (board) => {
  board = rotate(board);
  let newBoard = [];
  for (let i = 0; i < N; i++) {
    let now = board[i].filter((v) => v != 0);
    for (let j = 1; j < now.length; j++) {
      if (now[j] == now[j - 1]) {
        now[j - 1] *= 2;
        now[j] = 0;
      }
    }
    now = now.filter((v) => v != 0);
    while (now.length < N) {
      now.push(0);
    }
    newBoard.push(now);
  }
  return rotate(newBoard);
};

const goDown = (board) => {
  board = rotate(board);
  let newBoard = [];
  for (let i = 0; i < N; i++) {
    let now = board[i].reverse().filter((v) => v != 0);
    for (let j = 1; j < now.length; j++) {
      if (now[j] == now[j - 1]) {
        now[j - 1] *= 2;
        now[j] = 0;
      }
    }
    now = now.filter((v) => v != 0);
    while (now.length < N) {
      now.push(0);
    }
    newBoard.push(now.reverse());
  }
  return rotate(newBoard);
};

const goLeft = (board) => {
  let newBoard = [];
  for (let i = 0; i < N; i++) {
    let now = board[i].filter((v) => v != 0);
    for (let j = 1; j < now.length; j++) {
      if (now[j] == now[j - 1]) {
        now[j - 1] *= 2;
        now[j] = 0;
      }
    }
    now = now.filter((v) => v != 0);
    while (now.length < N) {
      now.push(0);
    }
    newBoard.push(now);
  }
  return newBoard;
};

const goRight = (board) => {
  let newBoard = [];
  for (let i = 0; i < N; i++) {
    let now = board[i].reverse().filter((v) => v != 0);
    for (let j = 1; j < now.length; j++) {
      if (now[j] == now[j - 1]) {
        now[j - 1] *= 2;
        now[j] = 0;
      }
    }
    now = now.filter((v) => v != 0);
    while (now.length < N) {
      now.push(0);
    }
    newBoard.push(now.reverse());
  }
  return newBoard;
};

const test = [
  [0, 4, 4, 32],
  [4, 0, 2, 64],
  [8, 8, 0, 0],
  [0, 16, 64, 4],
];

const test2 = [
  [4, 4, 4, 32],
  [8, 8, 2, 64],
  [0, 16, 64, 4],
  [0, 0, 0, 0],
];

const test3 = [
  [8, 4, 32, 0],
  [16, 2, 64, 0],
  [16, 64, 4, 0],
  [0, 0, 0, 0],
];

function threeTest(arr) {
  return goUp(goLeft(goDown(arr)));
}

function copyArray(array) {
  let arr = [];

  array.forEach((v) => {
    arr.push([...v]);
  });
  return arr;
}

let answer = 0;
let tmp2 = [];

function DFS(L, arr) {
  if (L === 5) {
    let tmp = [];
    arr.forEach((v) => tmp.push(Math.max(...v)));
    answer = Math.max(answer, Math.max(...tmp));
    return;
  } else {
    for (let i = 0; i < 4; i++) {
      if (i === 0) {
        let copyArr = copyArray(arr);
        tmp2.push("UP");
        DFS(L + 1, goUp(copyArr));
        tmp2.pop();
      } else if (i === 1) {
        let copyArr = copyArray(arr);
        tmp2.push("Right");
        DFS(L + 1, goRight(copyArr));
        tmp2.pop();
      } else if (i === 2) {
        let copyArr = copyArray(arr);
        tmp2.push("Down");
        DFS(L + 1, goDown(copyArr));
        tmp2.pop();
      } else if (i === 3) {
        let copyArr = copyArray(arr);
        tmp2.push("Left");
        DFS(L + 1, goLeft(copyArr));
        tmp2.pop();
      }
    }
  }
}

DFS(0, arr);
console.log(answer);
