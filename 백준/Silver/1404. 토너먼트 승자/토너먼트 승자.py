def main():
    import sys
    input_data = sys.stdin.read().split()
    # 28개의 정수를 읽습니다.
    nums = list(map(int, input_data))
    if len(nums) != 28:
        return

    # 8 x 8 승률 행렬 (소수로 저장)
    win_prob = [[0.0]*8 for _ in range(8)]
    idx = 0
    for i in range(8):
        for j in range(i+1, 8):
            p = nums[idx] / 100.0
            win_prob[i][j] = p
            win_prob[j][i] = 1 - p
            idx += 1

    # 각 참가자가 해당 브라켓에서 결승 진출할 확률 f[i] (라운드 1과 2를 이긴 확률)
    f = [0.0]*8
    # 브라켓 A: 참가자 0,1,2,3
    A0 = win_prob[0][1]  # 경기 0에서 0의 승리 확률
    A1 = win_prob[1][0]  # 경기 0에서 1의 승리 확률
    A2 = win_prob[2][3]  # 경기 1에서 2의 승리 확률
    A3 = win_prob[3][2]  # 경기 1에서 3의 승리 확률

    f[0] = A0 * ( A2 * win_prob[0][2] + A3 * win_prob[0][3] )
    f[1] = A1 * ( A2 * win_prob[1][2] + A3 * win_prob[1][3] )
    f[2] = A2 * ( A0 * win_prob[2][0] + A1 * win_prob[2][1] )
    f[3] = A3 * ( A0 * win_prob[3][0] + A1 * win_prob[3][1] )

    # 브라켓 B: 참가자 4,5,6,7
    B4 = win_prob[4][5]  # 경기 2에서 4의 승리 확률
    B5 = win_prob[5][4]  # 경기 2에서 5의 승리 확률
    B6 = win_prob[6][7]  # 경기 3에서 6의 승리 확률
    B7 = win_prob[7][6]  # 경기 3에서 7의 승리 확률

    f[4] = B4 * ( B6 * win_prob[4][6] + B7 * win_prob[4][7] )
    f[5] = B5 * ( B6 * win_prob[5][6] + B7 * win_prob[5][7] )
    f[6] = B6 * ( B4 * win_prob[6][4] + B5 * win_prob[6][5] )
    f[7] = B7 * ( B4 * win_prob[7][4] + B5 * win_prob[7][5] )

    # 결승에서의 승리 (토너먼트 우승) 확률 계산
    result = [0.0]*8
    # 브라켓 A의 참가자 (0~3)
    for i in range(0, 4):
        s = 0.0
        for j in range(4, 8):
            s += f[j] * win_prob[i][j]
        result[i] = f[i] * s
    # 브라켓 B의 참가자 (4~7)
    for i in range(4, 8):
        s = 0.0
        for j in range(0, 4):
            s += f[j] * win_prob[i][j]
        result[i] = f[i] * s

    # 출력 (절대/상대 오차 1e-9까지 허용)
    print(" ".join("{:.10f}".format(prob) for prob in result))
main()

