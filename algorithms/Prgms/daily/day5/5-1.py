# idx 가 queries 에 있는 값을 서로 바꿔주기
def solution(arr, queries):

    answer = arr

    for i, j in queries:
        answer[i], answer[j] = answer[j], answer[i]  #  말 그대로 arr[i]는 arr[j] 가 되고 arr[j]는 arr[i]가 된다.

    return answer


print(solution([0, 1, 2, 3, 4], [[0, 3], [1, 2], [1, 4]])) #  [3, 4, 1, 0, 2]

