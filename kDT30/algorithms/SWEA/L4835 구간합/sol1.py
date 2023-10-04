# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVFCzaqeUDFAWg

import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    n = N[1]  # list N 의 2 번째 값을 n 으로 설정, n 은 계산을 실행할 구간을 의미
    sum_num = []  # 구간의 합을 넣어줄 빈 셀

    for i in range(0, len(numbers)):  # 정수의 개수로 배열의 index 값을 설정
        if sum(numbers[i:i+n]) >= 0 and i+n <= len(numbers):  # 초기값 설정을 위함 + 구간을 지정
            sum_num.append(sum(numbers[i:i+n]))  # 더해준 값을 빈셀에 넣기

    result = max(sum_num) - min(sum_num)  # max, min 함수로 구분

    print(f'#{tc} {result}')
