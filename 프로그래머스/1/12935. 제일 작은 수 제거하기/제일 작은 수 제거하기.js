function solution(arr) {
    let newArr;
    if(arr.length==1){
        return [-1];
    }else{
        newArr=arr.filter((element)=>{
            return Number(element)!==Math.min(...arr)
        })
    }
    return newArr
}