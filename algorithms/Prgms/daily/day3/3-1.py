# https://school.programmers.co.kr/learn/challenges/training?order=acceptance_asc&statuses=unsolved&languages=python3
# mode 에 따른 값 도출 - 코드 처리하기 문제

def solution(code):
    mode = 0  # 시작 mode 는 0
    ret = ''  # 도출 값
    for idx in range(len(code)):  # code 의 idx 에 따른 값을 도출
        if mode == 0:
            if code[idx] == str(1):  # code 는 input 값이기 때문에 숫자 1은 문자 취급
                mode = 1  # code idx 값이 1일 경우 mode 변경
                ret = ret

            elif code[idx] != str(1) and idx % 2 == 0:  # 기준에 따라 문자를 추가
                ret += code[idx]

        elif mode == 1:
            if code[idx] == str(1):  # code idx 값이 1일 경우 mode 변경
                mode = 0

            elif code[idx] != str(1) and idx % 2:  # 기준에 따라 문자를 추가
                ret += code[idx]

    if ret == '':
        return 'EMPTY'  # 만약 반환되는 값이 없으면 empty 값을 도출
    else:
        return ret




print(solution("abc1abc1abc"))  # acbac