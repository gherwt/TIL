# t test 갯수
# n 양수의 갯수
import sys
# input 값을 input.txt 에서 가져오겠다.
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # x 가 우리가 원하는 숫자로 구성된 리스트 값으로 만들기 위함.
    numbers = list(map(int, input().split()))
    
    answer = max(numbers) - min(numbers)  # 0(2n) -> 0(n)

    max_val = min_val = numbers[0]

    print(f'#{tc} {answer}')


    
