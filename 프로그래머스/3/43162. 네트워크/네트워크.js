let arr;


function solution(n, computers) {
    const graph = Array.from({length:n+1}, () => [])
    let visited = Array.from({length:n+1}, () => 0)
    
    for(let i=0; i < n; i++){
        const computer = computers[i]
        for(let j=0; j < n; j++){
            if(computer[j] == 1){
                graph[i+1].push(j+1)
            }
        }
    }
    
    function dfs(L,node){
    for(const nextNode of graph[node]){
        if(visited[nextNode])continue
        visited[nextNode] = 1
        dfs(L+1, nextNode)
        }
    }
    
    let answer = 0
    
    for(let i=1; i <= n; i++){
        if(visited[i] == 0){
            dfs(0,i)
            answer+=1
        }
    }
    
    return answer
}