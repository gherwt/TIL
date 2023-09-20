# 스위치 총 개수
N = int(input())

# 스위치 초기 상태 리스트
switches = list(map(int, input().split()))

# 학생 수
case = int(input())

for _ in range(case):
    # 성별, 스위치 번호
    gender, num = map(int, input().split())
    # 스위치 번호 -> 인덱스로 변환
    idx = num - 1

    if gender == 1:  # 만약 남자 라면

        while idx < N:  # 현재 idx 가 N보다 작을 때만 실행
            switches[idx] = 0 if switches[idx] else 1  # 1 일때는 0, 0 일때는 1이 나온다.
            # switches[idx] ^= 1 과 같은 의미이다.
            idx += num  # 증가분을 생각해야 한다.

    else:
        # 일단, 받은 카드 번호를 바꾼다.
        switches[idx] ^= 1
        # 양 끝을 적용
        side = 1

        # 양 옆이 구간 내에 있을 때, 왼쪽은 0보다 크같, 오른쪽은 N보다 작음
        while 0 <= idx - side and idx + side < N:
            # 같으면 반복문 실행
            if switches[idx-side] == switches[idx+side]:
                # 양 옆 모두 바굼
                switches[idx-side] ^= 1
                switches[idx+side] ^= 1
                side += 1 # 양쪽을 한 칸 더 이동

             # 다르면 반복문 중단
            else:
                break

for line_no in range(N//20 + 2):
    start = 20 * line_no
    end = 20 * (line_no+1)
    print(*switches[start:end])  # 양 끝 리스트 기호를 지워주고 반환된다.