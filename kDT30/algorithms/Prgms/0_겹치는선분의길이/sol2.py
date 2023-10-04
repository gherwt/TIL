# https://school.programmers.co.kr/learn/courses/30/lessons/120876

# 1차원 평면은 -100 ~ 100임
# 보정으로 0 ~ 200 의 인덱스를 찾는 리스트로 표현 가능/ start + 100, end + 100 -> 사이값에 +1 를 해줘야한다. + range()
# 아직 선이 지나지 않으므로 모두 0
# lines를 순회하며 선이 지나가면 1씩 더함
# 이때 lines 의 시작 끝값을 보정(+100) 해줘야함
# 모든선의 표시를 끝내고
# 다시 처음부터 평면을 순회하며 겹치는 (1이상) 구간을 카운트함 if n >= 2 count(n)

def solution(lines):

    results = [set([]) for _ in range(201)] # 비어있는 집합자료형 만들기 함수 set([])-> 리스트를 만들어준다.
    count = 0

    for index ,line in enumerate(lines): # 인덱스, 값 부분으로 for 구문을 돌려주는 함수라고 생각하면 된다.
        x1, x2 = line
        for x in range(x1, x2):
            results[x + 100].add(index) # 100을 더해준다. 범위를 0 ~ 200 까지 설정했다.
    
    for line in results:
        if len(line) > 1:
            count += 1

    return count

print(solution([[0, 1], [2, 5], [3, 9]])) # 2
print(solution([[-1, 1], [1, 3], [3, 9]])) # 0
print(solution([[0, 5], [3, 9], [1, 10]])) # 8