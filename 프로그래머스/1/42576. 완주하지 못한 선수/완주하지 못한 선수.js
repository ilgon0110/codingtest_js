function solution(participant, completion) {    
    const pMap = new Map()
    const cMap = new Map()
    
    for(const p of participant){
        if(p in pMap){
            pMap[p] += 1
        } else {
            pMap[p] = 1
        }
    }
    
    for(const c of completion){
        pMap[c] -= 1
    }
    
    let answer = ''
    for(const k in pMap){
        if(pMap[k] > 0){
            answer = k
            break;
        }
    }
    
    return answer
}