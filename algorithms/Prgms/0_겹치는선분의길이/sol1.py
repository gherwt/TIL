# https://school.programmers.co.kr/learn/courses/30/lessons/120876

# 1차원 평면은 -100 ~ 100임 최대 200칸짜리 선분 이다.
# 보정으로 0 ~ 200 의 인덱스를 찾는 리스트로 표현 가능/ start + 100, end + 100 -> 사이값에 +1 를 해줘야한다. + range()
# 아직 선이 지나지 않으므로 모두 0
# lines를 순회하며 선이 지나가면 1씩 더함
# 이때 lines 의 시작 끝값을 보정(+100) 해줘야함
# 모든선의 표시를 끝내고
# 다시 처음부터 평면을 순회하며 겹치는 (1이상) 구간을 카운트함 if n >= 2 count(n)

# 선을  list 로 만들어 버린다.
def solution(lines):
    numbers = [0 for _ in range(201)]  # 0 ~ 200 범위의 평면, 칸
    # set을 사용???

    # 아직 선이 지나지 않기 때문에 모두 0을 가진다.
    for line in lines:
        start, end = line[0] + 100, line[1] + 100

        # start 부터 end 까지 idx 에 선이 그어진다고 보면 됨. => 겹친게 어딘지 보면 된다.
        for idx in range(start, end):
            # 이 리스트에 선이 지나가면서 1을 더해준다.
            numbers[idx] += 1

    answer = 0
    for num in numbers:
        if num >= 2:
            answer += 1

    return answer



print(solution([[0, 1], [2, 5], [3, 9]])) #
print(solution([[-1, 1], [1, 3], [3, 9]])) # 0
print(solution([[0, 5], [3, 9], [1, 10]])) # 8