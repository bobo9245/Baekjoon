function solution(s) {
    var answer = false;
    if (s.length==4 || s.length==6){
        if (/^\d+$/.test(s)){
            answer=true;
        }
    }
    return answer;
}