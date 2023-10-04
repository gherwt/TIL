import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    matrix = [[0 for i in range(10)] for j in range(10)]  # 10x10 고정된 범위 내에서

    N = int(input())  # 칠하는 횟수

    for _ in range(N):
        # 색칠하려는 도형의 시작 지점 [r1][c1] 끝지점 [r2][c2] 칠하려는 색깔: color
        r1, c1, r2, c2, color = map(int, input().split())  # 이렇게 저장하는 법 다시 생각하자.

        # 색칠하려는 도형의 범위를 설정
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):

                # row, col 칸에 색이 칠해져 있는데 현재 칠해진 색이 칠하려는 색깔이 아니라면?
                if matrix[r][c] and matrix[r][c] != color:
                    matrix[r][c] += color  # 색깔을 더 칠해준다.

                else:
                    matrix[r][c] = color  # 색칠해준다.

    # 보라색 개수 세기 -> 색칠 for 문이 끝나고 해주기 위해서 뺴줘야 한다. 그렇지 않으면 for 내에서 숫자를 세게 되고 초기화되지 않는다.
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 3:
                count += 1

    print(f'#{tc} {count}')

