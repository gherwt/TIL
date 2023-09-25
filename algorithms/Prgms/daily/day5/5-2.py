# k 보다 크면서 가장 작은 값을 찾기, 만약 값이 없으면 -1 도출
def solution(arr, queries):
    final = []
    for s, e, k in queries:
        answer = []
        for i in range(s, e+1):  # s, e 범위 내에서 k 보다 크면서 가장 작은 값을 찾기
            if arr[i] > k:
                answer.append(arr[i])  # k보다 큰 값을 도출

        if len(answer) == 0:  # k보다 큰 값이 없으면 -1 을 도출
            min_val = -1
        else:
            min_val = answer[0]  # k보다 큰 값들 중에서 최소값을 도출
            for j in range(len(answer)):
                if answer[j] < min_val:
                    min_val = answer[j]

        final.append(min_val)

    return final



print(solution([0, 1, 2, 4, 3],	[[0, 4, 2], [0, 3, 2], [0, 2, 2]]))  # [3, 4, -1]


