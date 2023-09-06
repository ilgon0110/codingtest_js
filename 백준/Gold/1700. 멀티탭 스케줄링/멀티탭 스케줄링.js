let fs = require("fs");
let _ = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

let [_N, ...arr] = _;

const N = Number(_N.split(" ")[0]);
arr = arr.map((v) => v.split(" ").map(Number)).flat();

let insert = [];
let cnt = 0;

for (let i = 0; i < arr.length; i++) {
  const now = arr[i];
  if (insert.includes(now)) continue;
  if (insert.length < N) {
    insert.push(now);
  } else {
    let target;
    let before = 0;
    insert.forEach((p) => {
      let next = Number.MAX_SAFE_INTEGER;
      for (let j = i + 1; j < arr.length; j++) {
        if (arr[j] === p) {
          next = j;
          break;
        }
      }
      if (before < next) {
        target = p;
        before = next;
      }
    });
    insert = insert.filter((v) => v !== target);
    insert.push(now);
    cnt++;
  }
}

console.log(cnt);
