# 배열 만들기 5
# s번 인덱스에서 시작하는 길이 l짜리 부분 문자열을 잘라내 정수로 변환합니다. 이때 변환한 정수값이 k보다 큰 값들을 담은 배열을 return 하는 solution 함수 만들기
def solution(intStrs, k, s, l):
    answer = []
    for num in intStrs:
        if int(num[s:s + l]) > k:
            answer.append(int(num[s:s + l]))
        elif int(num[s:s + l]) > k:
            answer.append(int(num[s:s + l]))

    return answer


print(solution(["0123456789", "9876543210", "9999999999999"], 50000, 5, 5))  # [56789, 99999]