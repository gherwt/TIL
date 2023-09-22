
# 수조작하기 1번 문제에서 파생된 문제
def solution(numLog):  # 숫자의 기록을 보고 글자를 도출하는 문제이다.
    answer = ''

    for num in range(1, len(numLog)):
        if numLog[num-1] - numLog[num] == -1:  # n 번째 - n-1 번째 = -1 이면 1을 더해준 것.
            answer += 'w'  # 그렇기 때문에 w 도출
        elif numLog[num-1] - numLog[num] == 1:  # n 번째 - n-1 번째 = 1 이면 1을 빼준 것임.
            answer += 's'   # 그렇기 때문에 s 도출
        elif numLog[num-1] - numLog[num] == -10:  # n 번째 - n-1 번째 = -10 이면 10을 더해준 것임.
            answer += 'd'  # 그렇기 때문에 d 도출
        elif numLog[num-1] - numLog[num] == 10: # n 번째 - n-1 번째 = 10 이면 10을 빼준 것임.
            answer += 'a'  # 그렇기 때문에 a 도출

    return answer






print(solution([0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]))  # "wsdawsdassw"
