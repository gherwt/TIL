def solution(a, b, c, d):
    nums = [a, b, c, d]
    counts = [nums.count(i) for i in nums]
    if max(counts) == 4:
        return a * 1111
    elif max(counts) == 3:
        p = nums[counts.index(3)]  # 특정 값의 index 를 확인한다.
        q = nums[counts.index(1)]  # 특정 값의 index 를 확인한다.
        return (10 * p + q) ** 2
    elif max(counts) == 2:
        if min(counts) == 2:
            if a == b:
                return (a + c) * abs(a - c)  # counts 값이 2인게 2개이므로 확인을 해줘야 한다.
            else:
                (a + b) * abs(a - b)
        else:
            q = nums[counts.index(1)]
            nums.remove(q)
            counts.remove(1)
            r = nums[counts.index(1)]
            # 최소 값이 2가 아니면 최대 값이 2인 경우이다. 이 경우, 3개의 숫자가 있기 때문에 p, q, r 이 존재한다.
            return q*r
    else:
        return min(nums)


# print(solution(2, 2, 2, 2))  # 2222
# print(solution(4, 1, 4, 4))  # 1681
# print(solution(6, 3, 6, 3))  # 27
print(solution(2, 5, 2, 6))  # 30
# print(solution(6, 4, 2, 5))  # 2