
def solution(num_list):
    answer = num_list
    i = len(num_list) - 1

    if num_list[i] > num_list[i-1]:  # 마지막 원소가 그전 원소보다 크면
         answer.append(num_list[i] - num_list[i-1])  # 마지막 원소에서 그전 원소를 뺀 값 추가

    else:  # 마지막 원소가 그전 원소보다 크지 않으면
        answer.append(num_list[i]*2)  #  마지막 원소를 두 배한 값을 추가


    return answer


print(solution([2, 1, 6]))   #  393
print(solution([5, 2, 1, 7, 5]))  # [5, 2, 1, 7, 5, 10]