# index 순서대로 글자 이어 붙이기

def solution(my_string, index_list):
    answer = ''
    for i in index_list:
        answer += my_string[i]

    return answer

print(solution("cvsgiorszzzmrpaqpe", [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]))  # "programmers"
print(solution("zpiaz"	, [1, 2, 0, 0, 3]))  # "pizza"