import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 배열 개수, 구간 개수 -> list 형식도 map 함수 사용이 가능하다.
    numbers = list(map(int, input().split()))

    max_val = min_val = sum(numbers[0:M])  # sum(numbers[:M] 사용도 가능 min, max 의 초기 값을 설정

    # 0 부터 m // 1부터 m+1.... // N-m 부터 N 까지 이기 때문에 n-m 개가 구간의 갯수이다.

    # start가 설정되면 end 로 할 수 있다.
    for start in range(N-M+1):
        end = start + M  # end 값은 start 값에 M 값을 계속 더한다. 어짜피 마지막 값은 N 이기 때문에
        total = sum(numbers[start:end])

        if total > max_val:
            max_val = total

        if total < min_val:
            min_val = total
