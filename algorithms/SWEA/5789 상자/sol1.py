import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())
    base = [0]*N

    for i in range(1, 1+Q):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            base[j] = L

    result = " ".join(map(str, base))
    print(f'#{tc} {result}')

    # T = int(input())
    #
    # for tc in range(1, T + 1):
    #     N, Q = map(int, input().split())
    #     base = [0] * N
    #
    #     for i in range(Q):
    #         L, R = map(int, input().split())
    #         for j in range(L - 1, R):
    #             base[j] = L
    #
    #     result = " ".join(map(str, base))
    #     print(f'#{tc} {result}')


