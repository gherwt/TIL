# 뒤에서부터 n 개의 글자를 도출하기
def solution(my_string, n):
    answer = my_string[len(my_string) - n:]

    return answer

print(solution("ProgrammerS123",11))  # "grammerS123"
print(solution("He110W0r1d",5))  # 	"W0r1d"