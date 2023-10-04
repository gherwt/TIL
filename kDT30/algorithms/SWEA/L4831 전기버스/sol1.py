
import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    # x 가 우리가 원하는 숫자로 구성된 리스트 값으로 만들기 위함.
    # K: 이동거리 N: 정류장 개수 M: 충전기 개수

    K, N, M = list(map(int, input().split()))
    stations = [False] * (N+1)  # 빈 리스트 [0] * (N+1)

    chargers = list(map(int, input().split()))
    for charger in chargers:  #  충전소의 위치를 설정해준다.
        stations[charger] = True

    current = K  # 현재 위치 (idx)
    count = 0  # 충전 횟수 (idx)
    last_charger = 0  # 마지막 충전 장소 (idx)

    # 현재 위치가 정류장 안에 있다 -> 정류장까지 이동하지 못했다.
    # 현재 위치가 종점 내에 있을 때, 종점에 도착하면 끝이 난다. 같으면 while 이 한번더 진행된다.
    while current < N:
        if stations[current]:  # 현재 위치가 충전소이면
            count += 1  # 충전을 한다.
            last_charger = current  # 마지막 충전 장소를 현재 장소로 갱신
            current += K  # 현재 위치에서 (K: 충전없이 갈 수 있는 최대 거리) 만큼 이동

        # 만약 충전소가 아니라면?
        else:
            current -= 1  # 현재 위치에서 앞으로 한 칸 이동한다.

        if current == last_charger:  # 만약 현재 위치가 마지막 충전소라면 최대 이동거리 내에 충전소가 없어 이동할 수 없다.
            count = 0
            break    # 실패 break


    print(f'#{tc} {count}')
