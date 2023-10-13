# 부분 문자열 이어 붙여 문자열 만들기
def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        my_string = my_strings[i]
        s, e = parts[i]
        answer += my_string[s:e+1]
    return answer







print(solution(["progressive", "hamburger", "hammer", "ahocorasick"], [[0, 4], [1, 2], [3, 5], [7, 7]]))  # "programmers"