import sys
from typing import List

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # x 가 우리가 원하는 숫자로 구성된 리스트 값으로 만들기 위함.
    K, N, M = list(map(int, input().split()))
    charge_stations = [0] + list(map(int, input().split())) + [N]
    location = 0  # 내가 있는 위치
    result = 0  # 충전 횟수

    for i in range(1, len(charge_stations)):
        dist = charge_stations[i] - charge_stations[i - 1]

        if dist > K:
            result = 0
            break

        elif dist + location <= K:
            location += dist

        else:
            result += 1
            location = dist

    print(f'#{tc} {result}')