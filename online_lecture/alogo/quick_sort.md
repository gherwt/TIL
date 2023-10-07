## 퀵 정렬

- 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법이다.
- 일반적인 상황에서 가장 많이 사용됨
- 병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘이다.

- 수행 과정

1. 가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터로 설정한다.
2. 왼쪽에서부터 큰 데이터를 찾고, 오른쪽에서부터 큰 데이터를 찾는다.
3. 그리고 큰 값을 오른쪽에 작은 값을 왼쪽에 넣어준다
    - 위치가 엇갈리는 경우 피벗과 작은데이터의 위치를 서로 변경한다.
4. 피벗 값의 위치가 중앙으로 옮겨진다.
   - 왼쪽은 피벗보다 작고 오른쪽은 피벗보다 크다.
   - 왼쪽 데이터 묶음 정렬 -> 왼쪽 데이터도 마찬가지로 정렬
   - 오른쪽 데이터 묶음 정렬 -> 오른쪽 데이터도 마찬가지로 정렬
   - 이상적인 경우 전체 연산 횟수를 O(NlogN) 을 기대할 수 있다.
   - 최악의 경우 N**2 의 시간복잡도를 가진다.

### 파이썬으로 구현

```
array =[]

def quick_sort(array, start, end):
    if start >= end # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right =  end
    while (left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while (left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복    
        while (rihgt > start and array[right] >= array[pivot]):
            right -= 1
        if (left > right): # 엇갈렸다면 작은데이터와 피벗을 교체한다.
            array[right], array[pivot] = array[pivot], array[rihgt]
        else: # 엇갈렸다면 작은데이터와 큰 데이터를 교체한다.
            array[left], array[pivot] = array[pivot], array[left]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행한다.
    quick_sort(array, start, right -1)
    quick_sort(array, right + 1, end)
quick_sort(array, 0, len(array) -1)
print(array)
```

### 파이썬의 장점을 살린 방식

```
# 파이썬의 장점을 살린 퀵 정렬

def quick_sort(array):
    # 리스트가 하나 이하의 원소를 가지면 종료
    if len(array) <= 1: return array 
    
    pivot, tail = array[0], array[1:]
    # 피벗은 첫 번째 원소, 피벗을 제외한 리스트는 tail

    leftSide = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    rightSide = [x for x in tail if x > pivot] # 분할된 오른쪽 부분
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환한다.
    return quick_sort(leftSide) + [pivot] + quick_sort(rightSide)
```

## 계수 정렬

- 특정한 조건이 부합할 때만 사용할 수 있지만, 매우 빠르게 동작하는 정렬 알고리즘이다.
  - 계수 정렬은 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능하다.
- 데이터의 개수가 N, 데이터(양수) 중 최댓값이 K일 때 최악의 경우에도 수행 시간 O(N+K)를 보장한다. 

1. 가장 작은 데이터부터 가장 큰 데이터까지의 범위가 모두 담길 수 있도록 리스트를 생성한다.
2. 데이터를 하나씩 확인하면서 데이터의 값과 동일한 인덱스의 데이터를 1씩 증가시킨다.
3. 결과적으로 최종 리스트에는 각 데이터가 몇 번씩 등장했는지 그 횟수가 기록된다.

- 결과를 확인할 때는 리스트의 첫번째 데이터부터 하나씩 그 값만큼 반복하여 인덱스를 출력합니다.


### 파이썬 계수 정렬

```
# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력

```


### 코드의 시간복잡도

- 계수 정렬의 시간 복잡도와 공간 복잡도는 모두 O(N+K)이다.
- 심각한 비효율성을 초래할 수 있다.
- 동일한 값을 가지는 데이터가 여러개 등장할 때 효과적으로 사용할 수 있다.