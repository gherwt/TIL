def solution(arr, queries):
    for s, e, k in queries:
        for i in range(s, e+1):  # s, e 범위 내에서 k의 배수 찾기 여기서 중요한 것은 0은 모든 정수의 배수이다. 모든 값에 0을 곱하면 0이기 때문이다.
            if i % k == 0:
                arr[i] += 1

    return arr


print(solution([0, 1, 2, 4, 3],[[0, 4, 1],[0, 3, 2],[0, 3, 3]]))  # [3, 2, 4, 6, 4]

