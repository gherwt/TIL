# 쇠막대기 자르기

# 괄호 () 형태이면 레이저를 쏘는 것

# ( 막대기의 시작 )막대기의 끝

# ()바로 붙어있으면 레이저인거임

# 레이저가 관통을 하는데 총 막대기의 갯수는 몇개인가??
# 5, 5, 7 => 17개


# 일단 ( 가
# ( 곱하기 별의 갯수
# 3 3 3
# 2 2 2
# 2
# *(((**)(*)*))(*)

# ( -> /
import sys

sys.stdin = open('input.txt')

T = int(input())
a = []
b = []
for tc in range(1, T+1):
    TC = input()
    laser = TC.replace('()','*')
    A = []
    B = []
    C = []
    D = []
    E = []
    count = 0
    star = 0
    line = 0

    for i in range(len(laser)):
        if laser[i] == '(':  # laser 에서 처음으로 나오는 ( 찾고 범위를 다시 설정하기.
            A.append(i)
        elif laser[i] == ')':
            B.append(i)
        elif laser[i] == '*':
            C.append(i)

    laser = laser[A[0]:]
    for b in range(len(B)):
        for a in range(len(A)):
            if b > a:
                for c in range(a, b+1):
                    if laser[c] == '*':
                        star += 1

                    elif laser[c] == '(':
                        line += 1
                result = star * line

                for d in range(len(C)):
                    e = laser[d:d+1].count(')')
                    result += (e*2)

    print(f'#{tc} {result}')
    #
    #
    #
    #      for a in range(len(A)):
    #           laser[A[a]]
    #
    # 이 범위에서 부터 ) 찾기 () 사이에 별 갯수 찾기 별 갯수에다가 ( 곱해주기 곱해주는 부분 보류
    # 첫/ 다음에 있는 ( 부터 2 번째 / 다음 별 갯수 찾기
    #  [333 2 2] /2 /2  (별+1)*( 갯수 / 다음 (부터 / 다음 별의 갯수 -> ( * 별 +1 -> 반복 마지막 (까지 이  범위에 있는 별을 다른 거로 변환
    # 그리고 첫별을 찾음 첫별 부터 다음 별까지 // 수 구하고 // * 2 해줌
    #  222 3  2  22  3
    #         count += 1  # 선분의 갯수를 센다.
    # for i in range(len(laser)):
    #     if laser[i] == '(':
    # for j in range(len(laser)):
    #     if laser[i] == ')':
    #           b.apend(i)
    # for s in range(-len(a),-1,0):
    #    for h in range(-len(a),-1,0):
    #      qwe = laser[s:h]
    #      qwer = qwe.count(*)
    # 333
    # 2 2 2 2
    #     elif laser[i] == '*':
    #         count += 1



# replace() -> * 별로 바꾼다. * 5개 쇠막대기 5개
# ((( () () ) (()) () )) (())
# (                    ) 5
#  (                  )  5
#   (       ) 3(  ) 2      (  ) 2
#
# 333
# 11
# 12
# 11
