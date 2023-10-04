# 이 방법 더 쉽다.

import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N: 전체 행렬 크기, M: 파리채 크기 MxM 크기의 파리채
    N, M = map(int, input().split())

    # 2차원 리스트를 표현한 것
    # matrix =[]
    # for _ in range(N):
    #   matrix.append(list(map(int, input().split())))

    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 최대/최소 초기값 설정 -> 최대는 가장 작은 값으로, 최소는 가장 큰 값으로. 그래서 나온 것이 무한대
    # float('INF') -> 무한대 값
    max_val = -float('INF')

    # row, col 은 파리채의 시작 최상단 idx, N-M+1 이 되는 이유는 mxm 크기이므로 index 값이 끝까지 갈 수 없기 떄문.
    for row in range(N-M+1):
        for col in range(N-M+1):

            total = 0  # for 문 내에서 초기화를 시켜줘야 하기때문에 for 문 내부에서 변수지정
            # 파리채 한번
            for r in range(M):
                for c in range(M):
                    total += matrix[row+r][col+c]

            if total > max_val:
                max_val = total

    print(f'#{tc} {max_val}')


# def hit(r_idx, c_idx, size):  # 결과로 내리쳤을 때 잡은 파리 수를 return
#
#     total = 0
#     for r in range(size):
#         for c in range(size):
#             total += matrix[r_idx + r][c_idx + c]
#
#     return total

