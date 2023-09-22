def solution(num_list):
    odd_number = ''
    even_number = ''

    for i in num_list:
        if i % 2:
            i = str(i)
            odd_number += i  # 문자 순서대로 이어 붙인다.
        else:
            i = str(i)
            even_number += i
    answer = int(odd_number) + int(even_number)  # 이렇게 이어붙인 수를 더해준다.

    return answer

print(solution([3, 4, 5, 2, 1]))  # 393
print(solution([5, 7, 8, 3])) # 581