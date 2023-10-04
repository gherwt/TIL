N = int(input())
switches = list(map(int, input().split()))
students = int(input())

for _ in range(students):
    gender, num = map(int, input().split())

    if gender == 1:  # 만약 남자 라면
        for n in range(num-1, N+1, num):
            switches[n-1] = 1 - switches[n-1]  # on 이면 off, off 면 on -> 1 - 0 = 1/ 1 - 1 = 0

    elif gender == 2:
        num = num - 1
        switches[num] = 1 - switches[num]  # on 이면 off, off 면 on 을 해준다.
        left = num - 1
        right = num + 1

        while left >= 0 and right < N and switches[left] == switches[right]:  # 받은 숫자 기준 양 쪽 값이 같을 경우
            switches[left] = 1 - switches[left]
            switches[right] = 1 - switches[right]
            left -= 1
            right += 1


for i in range(N):
    print(switches[i], end=' ')
    if (i + 1) % 20 == 0:  # 20 개를 기준, 줄 바꿔서 출력
        print()