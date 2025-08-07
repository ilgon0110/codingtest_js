function solution(friends, gifts) {
    var answer = 0;
    const map = new Map();
    const friendNames = new Set();
    const giftScores = new Map();
    const result = new Map();
    
    for (const friend of friends){
        map[friend] = new Map();
        giftScores[friend] = 0;
        result[friend] = 0;
        for (const f of friends){
            map[friend].set(f,0)
        }
    }
    
    for (const gift of gifts){
        const [a,b] = gift.split(' ');
        map[a].set(b, map[a].get(b)+1)
        giftScores[a] +=1
        giftScores[b] -=1
    }
    
    for (const a of friends){
        for (const b of friends){
            if (a === b)continue;
            const aScore = map[a].get(b)
            const bScore = map[b].get(a)
            if(aScore > bScore){
                result[a] += 1
            } else if (aScore === bScore){
                if(giftScores[a] > giftScores[b]){
                    result[a] +=1
                }
            }
        }
    }

    for (const f of friends){
        answer = Math.max(answer, result[f])
    }
    
    return answer;
}