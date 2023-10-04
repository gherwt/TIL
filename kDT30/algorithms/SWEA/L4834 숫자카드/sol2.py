# 구간합 접근법

# 문자열로 보는 방법

# '0123456789' -> count 한다.
# dic 로 저장
# 4-1 6-1 7-1 8-1 9-2
# {4:1, 9:2,  6:1 , 7:1} -> key, value 도출


# index 값으로 본다. list 10칸짜리 다 0으로 초기화
# 만약 있으면 +1 해준다 내가 푼 방법임. 0 ~ 9 까지

# ++ 최빈값이 같을 경우 같은 값 중에서 가장 큰 값을 도출한다.
# 0 이다가 갱신하는 방법
# max_val = 0 -> 1 찾으면 갱신, index 값도 저장 이걸 반복문 동안 반복

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    cards = list(map(int, input()))

    counter = [0 for _ in range(10)]  # 숫자 세기 위한 0 array 설정

    # or counter = [0]*10 사용 가능

    for card in cards:  # 카드 갯수를 세기
        counter[card] += 1

    max_card = 0  # 조건을 위해 max 설정
    max_count = counter[max_card]  # 최빈 값 count

    for idx in range(10):  # idx 값을 설정 -> 1~10 이어도 0~ 9가 index 이기 때문
        if counter[idx] >= max_count:  # 등장한 카드가 max 보다 같거나 크다면 갱신
            max_count = counter[idx]
            max_card = idx

    print(f'#{tc} {max_card} {max_count}')
