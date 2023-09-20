# # https://school.programmers.co.kr/learn/courses/30/lessons/120923



def solution(num, total): 
# # 3, 4, 5 = 3, 3 + 1, 3 + 2 12
# # 1, 2, 3, 4, 5 = 5-4, 5-3, 5-2, 5-1, 5 15
# # 2, 3, 4, 5 = 4-2, 4-1, 4, 4+1 14 
# # -1 0 1 2 3 =  5-6 , 5-5, 5-4, 5-3, 5-2 5    
# # 짝수면 /num 하고 끝값끼리 더하면 값이 같다.
# # 홀수면 /num -> 가운데 값을 뺴고 끝값을 더해주면 값이 같다.


# # 대충 짜보면 total%num: 홀수 -> total - (total//num = a)
# # (num - 1)//2 하고 짝수가 나옴. range(a-(num-1//2), a+(num-1//2))
# # 대충 a 로 나눈 값이 갯수인데..
# # 짝수는 total//(a, a+1) => 조합의 갯수(b)
# # (a+1)-b, a+b
    
    a = total//num
    if total % num == 0:
        answer = list(range(a-((num-1)//2), a+1+((num-1)//2)))
    
    else:
        b = total//(2*a+1)
        answer = list(range(a-b+1, a+b+1))

    return answer

print(solution(3, 12)) # [3, 4, 5]
print(solution(5, 15)) # [1, 2, 3, 4, 5]
print(solution(4, 14)) # [2, 3, 4, 5]
print(solution(5, 5)) # [-1, 0, 1, 2, 3]
