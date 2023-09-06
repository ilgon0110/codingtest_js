let fs = require("fs");
let _ = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

let [_N, ...arr] = _;

let [N, limit] = _N.split(" ").map(Number);

arr = arr.map((v) => v.split(" ").map(Number));
arr.shift();
arr.sort((a, b) => {
  if (a[1] === b[1]) {
    return a[0] - b[0];
  }
  return a[1] - b[1];
});

let answer = 0;
//각 인덱스에서 트럭에 실을 수 있는 택배의 갯수 = 여유 용량
const truck = Array.from({ length: N + 1 }, () => limit);

for (let v of arr) {
  const [start, end, weight] = v;
  let cargo = limit;
  //여유 용량 중 제일 작은 값으로 경로를 초기화해야함.
  for (let i = start; i < end; i++) {
    cargo = Math.min(cargo, truck[i]);
  }
  cargo = Math.min(cargo, weight);
  for (let i = start; i < end; i++) {
    truck[i] -= cargo;
  }
  answer += cargo;
}

console.log(answer);
