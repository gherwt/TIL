import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    nn_matrix = []  # 파리채 범위를 저장해 줄 빈셀을 설정
    max_val = 0  # 최대값을 구하기 위해 값을 설정
    r = N-M+1  # 파리채 범위를 고려한 칸의 범위
    M_2 = M**2  # 파리채 칸의 갯수

    for n in range(r):  # 범위 내에서
        for x in range(N):  # x 값
            for y in range(M):  # y 값
                if n + y < N:  # n+y 가 N보다 작을 때, 즉 범위를 벗어나지 않는 경우에만
                    nn_matrix.append(matrix[n+y][x])
                    # 열을 고정한 채 범위 내의 행만 움직인다.
                    # 이렇게하면 행이 n개씩 나오게 되는데 여기에 열을 n개 더해 nxn 의 사각형을 만든다.

        # 구한 사각형에서 범위를 잘 설정해줘야 한다.
        # 이유: 위의 식으로 구하면 겹친 부분이 발생하게 되고 겹치는 부분은 출력이 되지 않는다.
        # 그러므로 내가 직접 열을 옮기면서 작업해줘야 한다. 2차원이 아닌 1 차원으로 나타난다.
        # 그렇기 때문에 nxn 의 갯수를 구하고 그 갯수만 큼 묶어서 합을 구한다. 그러면서 동시에 한칸 이동
        # 앞 범위의 열만큼 이동하면 좌표상에서는 열 한칸을 이동한 효과가 발생한다.
        # 그리고 이렇게 밖에 빼주는 이유는 for 문에서 한 번에 작동하면 중간중간 오류가 발생하거나 누락되는 값이 생기 때문.
        for i in range(0, len(nn_matrix), M):
            if sum(nn_matrix[i:i+M_2]) > max_val:
                max_val = sum(nn_matrix[i:i+M_2])
        nn_matrix = []

    print(f'#{tc} {max_val}')
