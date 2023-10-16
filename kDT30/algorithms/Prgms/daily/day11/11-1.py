def solution(my_string):
    answer = []
    word = ''
    for i in range(1, len(my_string)+1):
        word = my_string[-i] + word
        answer.append(word)

    return sorted(answer)


print(solution("banana"))  # "a", "ana", "anana", "banana", "na", "nana"]