def solution(l, r):
    answer = []

    for i in range(l, r + 1):
        if all(num in ['0', '5'] for num in str(i)):  # all 함수 제네레이터를 활용해야 한다. num 을 정의하고 num 안에 0, 5 가 있는 지를 확인
                                                      # 여기서 num 은 뒤의 str 안에 있는 값이다. 가 뒤의 내용
            answer.append(i)

    if len(answer) == 0: #  없으면 -1 을 도출한다.
        answer.append(-1)

    return answer





print(solution(5,555))  # [5, 50, 55, 500, 505, 550, 555]
print(solution(10, 20))  # [-1]

