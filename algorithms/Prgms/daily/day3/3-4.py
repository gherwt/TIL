# https://school.programmers.co.kr/learn/challenges/training?order=acceptance_asc&statuses=unsolved&languages=python3

def solution(num_list):
    s = 1
    for i in num_list:
        s = i*s

    if sum(num_list)**2 > s:

        return 1

    else:
        return 0



print(solution([3, 4, 5, 2, 1]))  # 1
print(solution([5, 7, 8, 3]))  # 9

