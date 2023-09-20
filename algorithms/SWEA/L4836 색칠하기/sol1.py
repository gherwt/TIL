
import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    matrix = [[0 for i in range(10)] for j in range(10)]  # 10x10
    N = int(input())  # 칠하는 횟수
    idx = [list(map(int, input().split())) for _ in range(N)]

    count = 0

    for n in range(N):
        r1 = idx[n][0]  # 범위 시작 r 값
        c1 = idx[n][1]  # 범위 시작 c 값
        r2 = idx[n][2]  # 범위 끝 r 값
        c2 = idx[n][3]  # 범위 끝 c 값
        color = idx[n][4]    # 색깔

        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                if matrix[r][c] == 0:  # 색이 없을 때
                    matrix[r][c] = color   # 색칠하기

                elif matrix[r][c] != color:
                    matrix[r][c] = 3

    # for 문이 끝나고 세주기
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 3:
                count += 1

    print(f'#{tc} {count}')

