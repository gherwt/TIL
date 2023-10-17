# 접두사인지 확인하기
def solution(my_string, is_prefix):
    char = ''
    answer = []
    for i in range(len(my_string)):
        char += my_string[i]
        answer.append(char)

    if is_prefix in answer:
        return 1

    else:
        return 0

print(solution("banana", "ban"))  #  1
print(solution("banana",  "nan"))  # 0
print(solution("banana",	"abcd"))  # 0
print(solution("banana",	"bananan"))  # 0