
import sys
from typing import List

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # 범위가 되어줄 NxN 설정해줌.
    matrix = [[0 for _ in range(N)] for _ in range(N)]

    # delta index 순서를 배정해줘야 되기 때문에 순서가 중요
    # 문제에서 나온 우 하 좌 상을 row col 묶어서 표현.
    d_rows = [0, 1, 0, -1]
    d_cols = [1, 0, -1, 0]
    direction = 0  # -> [0, 1]  delta index 값임.

    # 현재의 좌표값
    row = col = 0

    # num -> 앞으로 채워줄 숫자.
    num = 1

    # 첫칸의 숫자는 채우고 시작
    # 채우고 전진 vs 전진하고 채우기
    # 전진가능? 채우고 turn
    matrix[row][col] = num

    # num 은 앞으로 채울 숫자

    while num != N ** 2:
        # 새로운 row/col 좌표값 작성
        new_row = row + d_rows[direction]
        new_col = col + d_cols[direction]

        # 새로운 좌표값은 0 이상 n 미만이고 채우려는 칸은 값이 비어있어야한다.

        if 0 <= new_row < N and 0 <= new_col < N and matrix[new_row][new_col] == 0:

            # 많이 볼 코드 순서가 너무나도 중요하다. 특히 순서가 중요. 왜나하면 빈값인지 확인하고 넣어야 하는지
            # 유효한 인덱스 범위를 확인한다. 유효한 행과 열 범위에 있는지 확인한다.
            # 해당 위치에 있는 값을 확인하여 특정 조건을 충족하는지 여부를 판단합니다.

            num += 1

            # 현재 좌표값을 새로운 좌표값으로 갱신한다.
            row, col = new_row, new_col

            # 새로운 좌표값에 num을 채운다.
            matrix[new_row][new_col] = num

        # 이 조건을 만족하지 않으면 (idx 범위 바깥이거나, 기존에 값이 있는 칸이라면)
        else:
            direction = (direction+1) % 4

        print(f'#{tc}')
        for i in range(N):
            print(*matrix[i])
