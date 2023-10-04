# https://school.programmers.co.kr/learn/challenges/training?order=acceptance_asc&statuses=unsolved&languages=python3
# 등차 수열의 특정한 항만 더하기

def solution(a, d, included):
    answer = 0  # 첫 항에서도 a 도출 가능

    for n in range(len(included)):
        if included[n] == True:
            answer += a + d * n  # 첫 항 a 에 (n-1)d 를 곱한 값을 더해준다. 하지만 range 함수를 사용한 idx 이기 때문에 0 부터 시작
                                 # n 을 곱해줘야 답이 도출

    return answer



print(solution(3, 4, [true, false, false, true, true])) # 37
print(solution(7, 1, [false, false, false, true, false, false, false])) # 10