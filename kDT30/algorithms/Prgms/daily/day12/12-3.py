
# 문자열의 앞의 n글자
def solution(my_string, n):
    answer = my_string[:n]
    return answer


print(solution("ProgrammerS123", 11))  # "ProgrammerS"
print(solution("He110W0r1d", 5))  # "He110"