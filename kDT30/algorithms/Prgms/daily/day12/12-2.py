# 접미사인지 확인하기
def solution(my_string, is_suffix):
    answer = []
    char = ''
    for i in range(1, len(my_string)+1):
        char = my_string[-i] + char
        answer.append(char)

    if is_suffix in answer:
        return 1

    else:
        return 0

print(solution("banana", "ana")) # 1
print(solution("banana", "wxyz"))  # 0
print(solution("banana", "nan"))  # 0
print(solution("banana", "abanana"))  # 0
