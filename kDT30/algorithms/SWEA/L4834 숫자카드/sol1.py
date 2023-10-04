# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVFCzaqeUDFAWg

import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    numbers = list(map(int, input()))  # 숫자를 한 자리씩 split 해준다.


    array_num = 10 * [0]  # 빈 10개의 빈 값을 지정.

    for i in numbers:
        if i in numbers:
            array_num[i] += 1  # 만약 숫자가 있으면 빈 array 값에 더 해준다. --> 카드가 몇 개 있는지 count

    max_array = array_num[0]  # 초기 값을 설정

    for s in range(len(array_num)):
        if array_num[s] >= max_array:  # 같, 커도 갱신이 된다.
            max_val = s  # 0 ~ 9 값이기 때문에(0부터 9까지 10개) index 값 = 현재 값이기 때문에
            # max 갱신할 때 s 를 그래돌 사용
            max_array = array_num[max_val]  # 카드가 나온 횟수 확인

    print(f'#{tc} {max_val} {max_array}')
