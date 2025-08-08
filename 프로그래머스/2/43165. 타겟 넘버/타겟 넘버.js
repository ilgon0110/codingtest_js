function solution(numbers, target) {
    var answer = 0;
    numbers.unshift(0)
    const N = numbers.length;
    
    function dfs(L,total){
        if(L===N-1){
            if(total === target){
                answer+=1
            }
            return
        }else{
            dfs(L+1, total+numbers[L+1])
            dfs(L+1, total-numbers[L+1])
        }
    }

    dfs(0,0)
    return answer;
}