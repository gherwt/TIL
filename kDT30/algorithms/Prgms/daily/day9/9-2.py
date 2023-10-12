def solution(my_string, queries):
    n = len(my_string)
    for s, e in queries:
        # [::-1] reverse 해준다.
        my_string = my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]

    return my_string

print(solution("rermgorpsam", [[2, 3], [0, 7], [5, 9], [6, 10]]))  # "programmers"

