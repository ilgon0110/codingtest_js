function solution(board) {
    var answer = 0;
    let dx = [-1,0,1,0];
    let dy = [0,-1,0,1];
    board = board.map(v => v.split(''));
    const N = board.length;
    const M = board[0].length;
    const visited = Array.from({length : N} , () => Array.from({length : M} , () => 0));
    const dist = Array.from({length : N} , () => Array.from({length : M} , () => 0));
    const ans = [];
    for(let i=0; i < N ; i++){
        for(let j=0; j < M; j++){
            if(board[i][j] === 'G'){ans.push(i,j); break;}
        }
    }
    const [ansX , ansY] = ans;

    for(let i=0; i < N; i++){
        for(let j=0; j < M; j++){
            if(board[i][j] === 'R'){
                visited[i][j] = 1;
                let queue = [];
                queue.push([i,j]);
                
                while(queue.length){
                    let [x,y] = queue.shift();
                    if(x === ansX && y === ansY)break;
                    for(let k=0; k < 4; k++){
                        let nx = dx[k] + x;
                        let ny = dy[k] + y;
                        let cnt = 0;
                        while(nx >= 0 && nx < N && ny >= 0 && ny < M && board[nx][ny] !== 'D'){
                            cnt++;
                            nx = dx[k]*cnt + x;
                            ny = dy[k]*cnt + y;
                        }
                        nx -= dx[k];
                        ny -= dy[k];
                        if(visited[nx][ny])continue;
                        visited[nx][ny] = 1;
                        dist[nx][ny] = dist[x][y] + 1;
                        queue.push([nx,ny])
                    }
                }
            }
        }
    }
    
    return dist[ansX][ansY] ? dist[ansX][ansY] : -1;
}