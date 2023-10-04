import sys

from pygments.lexers import j

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    R = K//2
    num = N-(K//2)

    for n in range(N):
        for j in range(R, num):
            if K % 2:
                if sum(puzzle[n][0:N]) >= K:
                    if sum(puzzle[n][j-R:j+R]) == K:
                        count += 1

            elif K % 2 == 0:
                if sum(puzzle[n][0:N]) >= K:
                    if sum(puzzle[n][j-R:j+R]):
                        count += 1

        for i in range(R, num):
            if K % 2:
                if sum(puzzle[0:N][n]) >= K:
                    if sum(puzzle[i-R:i+R][n]) == K:
                        count += 1

            elif K % 2 == 0:
                if sum(puzzle[0:N][n]) >= K:
                    if sum(puzzle[i-R:i+R][n]) == K:
                        count += 1

    print(f'#{tc} {count}')
