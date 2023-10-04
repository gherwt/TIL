# n 과 문자열 control 
# control wsda 로 구성 조건에 맞게 수를 도출하는 문제
def solution(n, control):
    for char in control:
        if char == 'w':
            n += 1
        elif char == 's':
            n -= 1
        elif char == 'd':
            n += 10
        elif char == 'a':
            n -= 10

    return n

print(solution(0,"wsdawsdassw"))  # -1