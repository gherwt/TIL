# https://school.programmers.co.kr/learn/challenges/training?order=acceptance_asc&statuses=unsolved&languages=python3
# 주사위 게임
def solution(a, b, c):

    if a == b == c:
        answer = (a+b+c) * (a**2+b**2+c**2) * (a**3+b**3+c**3)

    elif a != b and b != c and a != c:
        answer = a + b + c

    else:
        answer = (a + b + c) * (a ** 2 + b ** 2 + c ** 2)

    return answer




print(solution(2, 6, 1))  # 9
print(solution(5, 3, 3))  # 473
print(solution(4, 4, 4))  # 110592

