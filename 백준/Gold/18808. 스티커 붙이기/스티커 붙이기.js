let fs = require("fs");
let _ = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

let [input, ...arr] = _;
const [N, M, K] = input.split(" ");

arr = arr.map((v) => v.split(" ").map(Number));

const stickers = [];
const isCut = [0];
arr.forEach((v, idx) => {
  if (isCut.includes(idx)) {
    const [R, C] = arr[idx];
    const tmp = [];
    for (let i = 1; i <= R; i++) {
      tmp.push(arr[idx + i]);
    }
    stickers.push(tmp);
    isCut.push(idx + R + 1);
  }
});

const board = Array.from({ length: N }, () =>
  Array.from({ length: M }).fill(0)
);

const change90 = (sticker) => {
  const N = sticker.length;
  const M = sticker[0].length;
  const arr = [];
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      arr.push(sticker[i][j]);
    }
  }
  const RotateBoard = Array.from({ length: M }, () =>
    Array.from({ length: N }).fill(0)
  );
  let cnt = 0;
  for (let i = N - 1; i >= 0; i--) {
    for (let j = 0; j < M; j++) {
      RotateBoard[j][i] = arr[cnt];
      cnt++;
    }
  }
  return RotateBoard;
};

const isCanPut = (copyBoard, target) => {
  if (copyBoard.length !== target.length) return false;
  if (copyBoard[0].length !== target[0].length) return false;
  for (let i = 0; i < target.length; i++) {
    for (let j = 0; j < target[0].length; j++) {
      if (target[i][j] === 1 && copyBoard[i][j] !== 0) {
        return false;
      }
      if (target[i].length === 0) return false;
    }
  }
  return true;
};

for (let sticker of stickers) {
  const rotateSticker = [];
  for (let turn = 0; turn < 4; turn++) {
    if (turn === 0) {
      rotateSticker.push(sticker);
    } else {
      rotateSticker.push(change90(rotateSticker[turn - 1]));
    }
  }
  let isAlreadyPut = false;
  for (let target of rotateSticker) {
    const width = target[0].length;
    const height = target.length;

    //붙일 수 있는 지 확인
    if (isAlreadyPut) break;
    for (let i = 0; i < N; i++) {
      if (isAlreadyPut) break;
      for (let j = 0; j < M; j++) {
        let copyBoard = [];
        if (isAlreadyPut) break;
        for (let k = i; k < i + height; k++) {
          let tmp = [];
          if (isAlreadyPut) break;
          for (let l = j; l < j + width; l++) {
            if (isAlreadyPut) break;
            if (k < 0 || k >= N || l < 0 || l >= M) continue;
            tmp.push(board[k][l]);
          }
          copyBoard.push(tmp);
        }

        //copyBoard와 sticker 비교
        if (isCanPut(copyBoard, target)) {
          let tmp = [];
          target.forEach((v) => v.forEach((el) => tmp.push(el)));
          let cnt = 0;
          for (let x = i; x < i + height; x++) {
            for (let y = j; y < j + width; y++) {
              if (board[x][y] === 0) {
                board[x][y] = tmp[cnt];
              }
              cnt++;
            }
          }
          isAlreadyPut = true;
        }
      }
    }
  }
}

let answer = 0;
for (let i = 0; i < board.length; i++) {
  for (let j = 0; j < board[0].length; j++) {
    if (board[i][j] === 1) answer++;
  }
}

console.log(answer);
