# 이웃하는(연속하는) 값이라는 것이 중요하다. 
# +++ 중요한 것은 주어진 리스트 순서를 그대로 활용해야한다는 것.
# 5개를 골라야 한다. i 부터 5 개의 값을 저장 하나씩 저장
# slicing 을 이동하면 된다. list[0:x] 값, list[1:x+1] x+? 이 마지막일지를 고민
# 제일 작은 것도 구해야 한다.
# max , min 설정 -> max = a1 min =  a1 -> a2 비교해서 갱신
# 0-5 1-6 2-7 5-10 이걸 for 문에 넣기. 10 - 5 6개, 19칸 -> 2번
# 3? -> 규칙 찾기

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 배열 개수, 구간 개수 -> list 형식도 map 함수 사용이 가능하다.
    numbers = list(map(int, input().split()))

    max_val = min_val = sum(numbers[0:M])  # sum(numbers[:M] 사용도 가능 min, max 의 초기 값을 설정

    for i in range(0, len(numbers)-M+1):  # 계산 해줄 범위 설정
        if sum(numbers[i:i+M]) >= max_val:  # 구간이 max 보다 크거나 같으면 max
            max_val = sum(numbers[i:i+M])   # max 를 갱신

        elif min_val >= sum(numbers[i:i+M]):  # 구간이 min 보다 작거나 같으면
            min_val = sum(numbers[i:i+M])  # min 값을 갱신

    result = max_val - min_val

    print(f'#{tc} {result}')