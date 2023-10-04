# 전기 버스 문제 접근법
#
#
import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    # x 가 우리가 원하는 숫자로 구성된 리스트 값으로 만들기 위함.
    K, N, M = list(map(int, input().split()))  # input 한 값을 숫자로 변환해준다.
    charge_stations = [0] + list(map(int, input().split())) + [N]  # 0(출발지에서 충전하고 시작한다.) 과 종점을 충전소에 포함해준다.
    count = 0  # 충전 횟수
    current = 0  # 현재 위치

    for i in range(1, len(charge_stations)):  # range 함수이기 -1을 해줄 필요가 없다. + 정류소를 숫자에 맞게 배치해준다.
        dist = charge_stations[i] - charge_stations[i - 1]  # 충전소 사이의 거리

        if dist > K:  # 충전소 사이의 거리가 K 보다 크면 이동할 수 없다.
            count = 0
            break

        if dist + current <= K:  # 이동 거리를 따져준다. dis + current = 이동거리 즉, 이전 정류소에서 얼마나 이동했는지 현재 위치를 말해줌
            current += dist  # 이동한 거리를 따져준다. 즉 한번 충전하고 이동한 거리를 구한다. 이동 거리가 한번 충전시 K 까지는 이동할 수 있기 때문에 K까지 포함해주는 것
            # 현재 위치를 도출해 내서 이동한 거리와 K 를 비교해 충전 여부를 판단하는 문제였다.

        else:
            current = dist  # 충전 후의 이동 거리를 갱신
            count += 1  # 갱신 후에 충전 횟수 + 1 해준다.

    print(f'#{tc} {count}')
