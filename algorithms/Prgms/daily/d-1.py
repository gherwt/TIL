def solution(num1, num2):

    answer = num1%num2  #  나머지를 구하는 함수

    return answer



print(solution(3,2)) # 1
print(solution(10, 5))  # 0


def solution(array):
    answer = sorted(array, reverse=True)
    mid = len(array) // 2    #  중앙값을 구해주기
    answer = answer[mid]

    return answer

print(solution([1, 2, 7, 10, 11])) # 7
print(solution([9, -1, 0]))  # 0