
# 1 = on, 0 = off
# 남자 - 스위치 번호가 자기가 받은 수의 배수 - > 스위치 상태를 변경
# 여자 - 스위치 번호가 붙은 스위치를 중심으로 좌우가 대칭, 가장많은
#        스위치를 포함하는 구간의 스위치를 바꿈 -> 항상 홀수
#        만약 좌우가 다르면 뽑은 스위치만 바꾼다.

N = int(input())
on_off = list(map(int, input().split()))
num = int(input())
students = [list(map(int, input().split())) for _ in range(num)]
# map 함수 한 꺼번에 묶어서 처리해준다는 의미이다. + input. split 입력값을 일정 기준에 따라 나누어준다.
# map(int, ~) input 값을 모두 int 처리해준다.
# [list for _ in range(num)]
# num 범위에 있는 값을 리스트화 시켜준다.
# 이렇게 리스트화 한 값을 gender, number 값으로 나누어준다.

for gender, number in students:
    # number = number - 1 여기서 안하는 이유 배수 값을 입력하는 것이기 때문에
    # 여기서 -1 해버리면 생각했던 값이 도출이 되지 않는다.
    if gender == 1:
        for i in range(number, N+1, number): # 지정 숫자, range 이기떄문에 N + 1 값, number 마다는 배수를 의미한다.
            on_off[i-1] = 1 - on_off[i-1] # 이게 핵심 어짜피 0, 1 값이므로 1을 기준으로 빼주면 됨 
            # 만약 인덱스에 있는 값이 1이면 1 - 1 되서 0이됨 즉, 0으로 전환되는 효과
            # 만약 0이면 1-0 이므로 1이 도출.
            # 생각보다 단순함. 생각의 전환이 필요하다.

    elif gender == 2:
       number -= 1  # 3의 인덱스가 2 이므로 계산하기 쉽게 바꿔준다. 이제는 배수 계산이 아닌 양쪽 끝값 비교이기때문에 -1 해도 무방
       on_off[number] = 1 - on_off[number]
       left = number - 1
       right = number + 1
       # while 문 활용을 생각할것. ~~동안 즉 조건이 충족하는 동안 돌린다는 의미
       while left >= 0 and right < N and on_off[left] == on_off[right]:
           on_off[left] = 1 - on_off[left]
           on_off[right] = 1 - on_off[right]
           left -= 1 # 왼쪽과 비교하기 때문에 1씩 감소
           right += 1 # 오른쪽과 비교하기 때문에 1씩 증가

for i in range(N):
    print(on_off[i], end=' ')
    if (i + 1) % 20 == 0:
        print()

## 이 문제는 나중에 꼭 다시 풀기.

        