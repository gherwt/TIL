# 특정 문자열 거꾸로
# 특정 문자열 거꾸로
def solution(my_string, s, e):
    answer = my_string[:s] + my_string[s:e+1[:-1] + my_string[e+1:]
    return  answer

print(solution("Progra21Sremm3",6,12))  # ProgrammerS123
print(solution("Stanley1yelnatS", 4, 10))  # Stanley1yelnatS