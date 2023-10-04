# t test 갯수
# n 양수의 갯수
import sys
# input 값을 input.txt 에서 가져오겠다.
sys.stdin = open('input.txt')

# 0(2n) -> 0(n) 계산 횟수를 줄이는 방식
# min, max 함수는 연산 과정을 한 번 더 거치기 때문에 효율성을 위해서 새로운 방법도 생각할 필요가 있다.
T = int(input())

for tc in range(1, T+1):
    N = int(input())

    numbers = list(map(int, input().split()))

    max_val = min_val = numbers[0]  # 리스트 내의 min, max 를 비교하기 위한 초기값을 설정

    for num in numbers:

        if num > max_val:  # max_val 이 num 보다 작으면 num 을 max_val 로 지정
            max_val = num

        elif num < min_val:  # min_val 이 num 보다 크면 num 을 min_val 로 지정
            min_val = num

    answer = max_val - min_val

    print(f'#{tc} {answer}')