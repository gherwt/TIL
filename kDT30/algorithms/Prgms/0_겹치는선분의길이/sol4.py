# 집합을 활용해서 사용하기
def solution(lines):
    line1 = set(i for i in range(lines[0][0], lines[0][1]))
    line2 = set(i for i in range(lines[1][0], lines[1][1]))
    line3 = set(i for i in range(lines[2][0], lines[2][1]))
    return len((line1 & line2) | (line2 & line3) | (line1 & line3))

print(solution([[0, 1], [2, 5], [3, 9]])) # 2
print(solution([[-1, 1], [1, 3], [3, 9]])) # 0
print(solution([[0, 5], [3, 9], [1, 10]])) # 8