n,m = map(int,input().split())
def count_min_eights(L: int, R: int) -> int:
    # 문자열로 변환
    sL = str(L)
    sR = str(R)
    
    # 자릿수가 다르면 최소 8의 개수는 0
    if len(sL) != len(sR):
        return 0
    
    # 공통 접두사에서 8의 개수를 센다
    common_eight_count = 0
    for i in range(len(sL)):
        if sL[i] == sR[i]:
            if sL[i] == '8':
                common_eight_count += 1
        else:
            break  # 접두사가 다르면 종료
    
    return common_eight_count
print(count_min_eights(n,m))