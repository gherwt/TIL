# https://school.programmers.co.kr/learn/challenges/training?order=acceptance_asc&statuses=unsolved&languages=python3
#
# def solution(array):
#     count_list = [0] * (max(array) + 1)  # index 값으로 최빈값을 구하기
#
#     for i in array:
#         count_list[i] += 1  # 숫자의 갯수를 세어서 index 값에 할당해준다.
#
#     max_count = max(count_list)  # 최빈 값의 갯수를 구한다.
#     max_num = 0
#     num = 0
#
#     for j in range(len(count_list)):
#         if max_count == count_list[j]:  # 최빈 값이 여러 개인지 확인하기 위함이다.
#             max_num = j
#             num += 1
#
#     if num > 1:
#         return -1
#     else:
#         return max_num  # index 값으로 설정한 값에 저장했기 때문에 j 값이 최빈값이라고 할 수 있다.
#
#
#
#
#     # print(array_dict)
#
#
# print(solution([1, 2, 3, 3, 3, 4]))  # 3
# print(solution([1, 1, 2, 2]))  # -1
# print(solution([1]))  # 1


# def solution(n):
#         answer = []
#         numbers = list(range(1, n + 1))
#         for num in numbers:
#             if num % 2:
#                 answer.append(num)
#
#         return answer
#
# print(solution(10))  # [1, 3, 5, 7, 9]
# print(solution(15))  # [1, 3, 5, 7, 9, 11, 13, 15]


# def solution(n):
#     if n % 7 == 0:
#         answer = n // 7
#
#     else:
#         answer = n // 7 + 1
#
#     return answer


# def solution(n):
#     min_val = min(6, n)
#     pizza = 0
#
#     for i in range(min_val, 6 * n + 1):
#         if i % 6 == 0 and i % n == 0:
#             pizza = i // 6
#             break
#     return pizza
#
# print(solution(6)) 	# 1
# print(solution(10)) # 5
# print(solution(4)) 	# 2