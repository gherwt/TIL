def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        elif arr[i] > stk[-1]:
            stk.append(arr[i])
            i += 1
        elif stk[-1] >= arr[i]:
            stk.pop()

    return stk

print(solution([1, 4, 2, 5, 3]))  # [1, 2, 3]