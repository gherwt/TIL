
# 시작 번호부터 끝 번호까지의 숫자로 이루어진 리스트 만들기

def solution(start_num, end_num):
    answer = []
    for i in range(start_num,end_num+1):
        answer.append(i)

    return answer


print(solution(3, 10)) [3, 4, 5, 6, 7, 8, 9, 10]